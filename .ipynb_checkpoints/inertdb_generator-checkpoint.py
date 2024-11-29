#!/usr/bin/env python
# coding: utf-8

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import tensorflow as tf
from rdkit import Chem, RDLogger
from rdkit.Chem.Scaffolds import MurckoScaffold
from rdkit.Chem import AllChem
from scipy.spatial.distance import cosine as cos_distance
from collections import Counter
from tqdm import tqdm
import pickle
import argparse

physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    for device in physical_devices:
        tf.config.experimental.set_memory_growth(device, True)
    print(f"Configured memory growth for {len(physical_devices)} GPU(s).")
else:
    print("No GPUs available. Skipping GPU configuration.")

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Generate SMILES (generated inactive compounds, GIC) using a trained model on InertDB-CIC (curated inactive compounds).")
parser.add_argument(
    "-n", 
    "--num_generations", 
    type=int, 
    default=2, 
    help="Number of times to run the generation, each generating 1,000 SMILES (default: 2 = 2,000 SMILES strings)"
)
parser.add_argument(
    "-o", 
    "--output_file", 
    type=str, 
    default="gic.txt", 
    help="Name of the output file to save the generated valid/unique SMILES strings (default: gic.txt)"
)
args = parser.parse_args()

TRAIN_SET = './data/inertdb_cic_v2024.03.smi'
OUTPUT_FILE = args.output_file

# Helper Functions
def load_vocab(vocab_file):
    """Load vocabulary from a pickle file."""
    with open(vocab_file, 'rb') as f:
        return pickle.load(f)

def is_valid_smiles(smiles):
    RDLogger.DisableLog('rdApp.*')  
    mol = Chem.MolFromSmiles(smiles)
    RDLogger.EnableLog('rdApp.*')
    return mol is not None

def filter_valid_smiles(smiles):
    """Filter out invalid SMILES."""
    validity = [is_valid_smiles(s) for s in smiles]
    valid_smiles = [i for (i, v) in zip(smiles, validity) if v]
    return valid_smiles

def canonicalize_smiles(smiles):
    """Canonicalize SMILES strings."""
    canonical_smiles = []
    for smi in smiles:
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:
            canonical_smiles.append(Chem.MolToSmiles(mol))
        else:
            canonical_smiles.append(None)
    return canonical_smiles

def dict_count(smiles):
    """Count occurrences of each SMILES in a dictionary."""
    smiles = Counter(smiles)
    if None in smiles:
        smiles.pop(None)
    return smiles

def generate_scaffs(smiles, min_rings=2):
    """Generate Murcko scaffolds."""
    scaffolds = []
    if(len(smiles) > 1000):
        smiles = smiles[:1000]
    for smi in smiles:
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:  # Ensure the molecule could be parsed
            try:
                scaffold = MurckoScaffold.GetScaffoldForMol(mol)
            except (ValueError, RuntimeError):
                scaffolds.append(None)
                next
            n_rings = scaffold.GetRingInfo().NumRings()
            scaffold_smi = Chem.MolToSmiles(scaffold)
            if scaffold_smi == '' or n_rings < min_rings:
                scaffolds.append(None)
                next
            scaffolds.append(scaffold_smi)
    return scaffolds

def generate_frags(smiles):
    """Generate fragments from SMILES using BRICS bonds."""
    fragments = []
    if(len(smiles) > 1000):
        smiles = smiles[:1000]
    for smi in smiles:
        mol = Chem.MolFromSmiles(smi)
        if mol is not None:  # Ensure the molecule could be parsed
            frags = AllChem.FragmentOnBRICSBonds(mol)
            frags_smi = Chem.MolToSmiles(frags).split(".")
            fragments.extend(frags_smi)
    return fragments

def cos_similarity(ref_counts, gen_counts):
    """Calculate cosine similarity between two dictionaries.
     sim = <r, g> / ||r|| / ||g||
    """
    if len(ref_counts) == 0 or len(gen_counts) == 0:
        return np.nan
    keys = np.unique(list(ref_counts.keys()) + list(gen_counts.keys()))
    ref_vec = np.array([ref_counts.get(k, 0) for k in keys])
    gen_vec = np.array([gen_counts.get(k, 0) for k in keys])
    return 1 - cos_distance(ref_vec, gen_vec)

def save_smiles(smiles, filename):
    """Save SMILES to a file."""
    with open(filename, 'w') as f:
        f.writelines(f"{s}\n" for s in smiles)

# Load Data
try:
    print("Loading training data...")
    with open(f"{TRAIN_SET}", 'r') as file:
        reference_SMILES = file.read().strip().split('\n')
    reference_SMILES = canonicalize_smiles(reference_SMILES)
    print("Training data loaded successfully.")
except Exception as e:
    print(f"Error: Failed to load training data. {e}")
    raise

try:
    print("Loading vocabulary...")
    vocab = load_vocab('./model/vocab.pkl')
    ids_from_chars = tf.keras.layers.StringLookup(vocabulary=list(vocab), mask_token=None)
    chars_from_ids = tf.keras.layers.StringLookup(
        vocabulary=ids_from_chars.get_vocabulary(), invert=True, mask_token=None
    )
    print("Vocabulary loaded successfully.")
except Exception as e:
    print(f"Error: Failed to load vocabulary. {e}")
    raise

# Load Model
try:
    print("Loading trained model...")
    one_step_model = tf.saved_model.load('./model/model_checkpoints')
    print("Trained model loaded successfully.")
except Exception as e:
    print(f"Error: Failed to load model. {e}")
    raise

# Generation Functions
def generate():
    """Generate 1,000 SMILES using the loaded model."""
    states = None
    next_char = tf.constant(['^']*1000)
    result = [next_char]
    
    for n in range(1000):
        next_char, states = one_step_model.generate_one_step(next_char, states=states)
        result.append(next_char)
    
    result = tf.strings.join(result).numpy().astype('<U')
    return np.char.replace(np.char.replace(result, '^', ''), '_', '').tolist()

def generate_n_times(n=1):
    """Generate n*1,000 SMILES."""
    result = []
    for _ in tqdm(range(n), desc="Generating SMILES strings ... ", bar_format='{l_bar}{bar:40}{r_bar}{bar:-40b}'):
        result.extend(generate())
    return result

def compute_metrics(result, reference):
    """Compute performance metrics."""
    valid_smiles = filter_valid_smiles(result)
    l = min(10000, len(result))
    metrics = {
        "validity": len(valid_smiles) / len(result),
        "unique@1k": len(set(result[:1000])) / 1000,
        "unique@10k": len(set(result[:l])) / l,
        "novelty": 1 - len(set(valid_smiles[:l]).intersection(reference)) / len(valid_smiles),
        "scaffold_similarity": cos_similarity(
            dict_count(generate_scaffs(valid_smiles)),
            dict_count(generate_scaffs(reference))),
        "fragment_similarity": cos_similarity(
            dict_count(generate_frags(valid_smiles)),
            dict_count(generate_frags(reference))),
    }
    return {k: round(v, 4) for k, v in metrics.items()}

# Generate and evaluate
generated_SMILES = generate_n_times(args.num_generations)

metrics = compute_metrics(generated_SMILES, reference_SMILES)

print('\nGeneration performances:')
print('Validity:\t', metrics['validity'])
print('Unique@1K:\t', metrics['unique@1k'])
print('Unique@10K:\t', metrics['unique@10k'])
print('Novelty:\t', metrics['novelty'])
print('Scaffold similarity (Scaff):\t', metrics['scaffold_similarity'])
print('Fragment similarity (Frag):\t', metrics['fragment_similarity'])

valids = filter_valid_smiles(generated_SMILES)
print(f'\n... {len(valids)} valid SMILES were generated')
valcan = canonicalize_smiles(valids)
valcanuniq = [i for i in valcan if i not in reference_SMILES]

save_smiles(valcanuniq, OUTPUT_FILE)
print(f'... {len(valcanuniq)} unique SMILES were generated ... saved as {OUTPUT_FILE}')
