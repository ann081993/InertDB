# InertDB
A Comprehensive Database of Biologically Inactive Compounds

<p align="center">
  <img src="/GA.png" width="75%" height="75%" title="InertDB-overview">
</p>

## Overview
**InertDB** is a curated chemical database designed to address the lack of biologically inactive compounds in predictive modeling for AI-based drug discovery. This limitation often leads to biased datasets dominated by active compounds, reducing the diversity and robustness of machine learning models.

InertDB bridges this gap by providing:
- [**Curated Inactive Compounds (CICs)**](https://github.com/ann081993/InertDB/blob/main/data/inertdb_cic_v2024.03.smi): 3,205 inactive compounds rigorously curated from [PubChem BioAssays](https://pubchem.ncbi.nlm.nih.gov/docs/bioassays).
- [**Generated Inactive Compounds (GICs)**](https://github.com/ann081993/InertDB/blob/main/data/inertdb_gic_v2024.03.smi): 64,368 potential inactive compounds generated using deep generative AI trained on the CICs.
By offering a comprehensive resource for biologically inactive small molecules and expanding the chemical space with GICs, Inert DB aims to enhance the robustness and accuracy of predictive AI models in toxicology and pharmacology.

## Key Features
- Diverse Assays: **CICs** are extracted from over 260 million PubChem bioassay results, leveraging an NLP-based assay diversity metric.
- AI-Generated Inactives: **GICs** supplement chemical space using RNN-based deep generative AI (`inertdb_generator.py`).
- Low PAINS Content: Minimizes frequent false positives in high-throughput screening.
- Drug-Like Properties: CICs exhibit physicochemical properties comparable to approved drugs.
- Validated Performance: Predictive modeling benchmarks ([LIT-PCBA](https://drugdesign.unistra.fr/LIT-PCBA/) and [MUV](https://www.tu-braunschweig.de/en/pharmchem/forschung/baumann/translate-to-english-muv)) show significant improvements.

## Repository Structure
```
InertDB/
├── data/                 # Pre-processed datasets of CICs and GICs
│   ├── inertdb_cic_v2024.03.smi
│   ├── inertdb_gic_v2024.03.smi
│
├── inertdb_generator.py  # Script for generating additional GICs
├── README.md             # Project documentation (this file)
```

## Usage
### 1. Download Pre-Processed InertDB Datasets
Download the CICs and GICs datasets:
```bash
wget https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_cic_v2024.03.smi
wget https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_gic_v2024.03.smi
```

### 2. Generate Additional GICs
Use the provided script to generate new GICs using the pre-trained generative AI model.
#### 1. Requirements
Ensure the following Python packages are installed, or install the dependencies from `requirements.txt`:
- `tensorflow`
- `numpy`
- `rdkit`
```bash
conda create -n inertdb python=3.10
conda activate inertdb
pip install -r requirements.txt
```

#### 2. Run the Script
Generate additional GICs by specifying the number of iterations:
```bash
python inertdb_generator.py -n NUM_GENERATIONS -o OUTPUT_FILE
```
- `NUM_GENERATIONS`: Number of iterations to generate (each iteration produces 1,000 SMILES).
- `OUTPUT_FILE`: Name of the file to save the generated GICs (default: `gic.txt`).

Example:
```bash
python inertdb_generator.py -n 5 -o my_gics.txt
```
This generates up to 5,000 SMILES strings and saves the valid, unique SMILES to `my_gics.txt`.

## Citation
- If you use **InertDB** in your research, please considering citing the following publication:
```
@article{An2025,
  author    = {Seungchan An and Yeonjin Lee and Junpyo Gong and Seokyoung Hwang and In Guk Park and Jayhyun Cho and Min Ju Lee and Minkyu Kim and Yun Pyo Kang and Minsoo Noh},
  title     = {InertDB as a generative AI-expanded resource of biologically inactive small molecules from PubChem},
  journal   = {Journal of Cheminformatics},
  year      = {2025},
  volume    = {17},
  pages     = {49},
  doi       = {10.1186/s13321-025-00999-1},
  url       = {https://doi.org/10.1186/s13321-025-00999-1}
}
```

## License
This InertDB is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc].
This curated dataset is freely available for academic and non-commercial research purposes. For commercial use, a license agreement is required. Please contact [ann081993 at snu dot ac dot kr] for or refer to the [LICENSE](https://github.com/ann081993/InertDB/blob/main/LICENSE) for details.

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg

<meta name="google-site-verification" content="ej7qLx-MFVuGfYCVNGfU4aOGo__8AZDQ2af9dBM_Krw" />
