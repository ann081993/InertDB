# InertDB
A Comprehensive Database of Biologically Inactive Compounds

<p align="center">
  <img src="/GA.png" width="75%" height="75%" title="InertDB-overview">
</p>

## Overview
**InertDB** is a curated chemical database that addresses the lack of data on biologically inactive compounds, a critical gap for predictive models in AI-based drug discovery. Traditional datasets often exhibit a publication bias favoring active compounds, limiting the diversity of training data for predictive models. InertDB provides access to both curated inactive compounds (CICs) identified from PubChem and generated inactive compounds (GICs) derived using deep generative AI.
- [**CICs**](https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_gics.txt): 3,205 inactive compounds rigorously curated from [PubChem BioAssays](https://pubchem.ncbi.nlm.nih.gov/docs/bioassays).
- [**GICs**](https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_gics.txt): 64,368 potential inactive compounds generated using deep generative AI trained on the CICs.
By offering a comprehensive resource for biologically inactive small molecules and expanding the chemical space with GICs, Inert DB aims to enhance the robustness and accuracy of predictive AI models in toxicology and pharmacology.

## Key Features
- [**Curated Inactive Compounds (CICs)**](https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_gics.txt): Extracted from over 260 million bioassay results, ensuring high assay diversity.
- [**Generated Inactive Compounds (GICs)**](https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_gics.txt): Developed using RNN-based depp generative models to supplement chemical space.
- **Reduced PAINS**: A low proportion of PAINS to minimize false positives in high-throughput screening.
- **Drug-like Properties**: Majority of the CICs exhibit comparable physicochemical properties to approved drugs.
- **Validation-Backed**: Demonstrated improved performance in predictive models using benchmark datasets ([LIT-PCBA](https://drugdesign.unistra.fr/LIT-PCBA/) and [MUV](https://www.tu-braunschweig.de/en/pharmchem/forschung/baumann/translate-to-english-muv))

## Applications
- *False Positive Reduction* in **Virtual Screening Library**: Provides a rich set of structurally diverse and pharmacologically relevant inactive compounds, while minimizing off-target activities, improving the precision of drug discovery efforts. 
- **AI-Driven Drug Discovery** (predictive modeling, QSAR, molecular property prediction ...): Enhances predictive models by addressing bioactivity bias and supplementing training data with reliable inactive compunds.
- Predictive Modeling: Enhance the performance of machine learning models in predicting biological activity by incorporating reliable inactive compounds from InertDB.

## Repository Structure

## Download
### Only InertDB compounds
```bash
wget https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_cics.txt
wget https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_gics.txt
```

### Getting started with generative AI for inactive compounds
1. Clone the repository:
```bash
git clone https://github.com/ann081993/InertDB.git
cd InertDB
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Explore the data: the CICs and GICs are available in the `data/` directory as `.txt` files.
```python
cics = pd.read.csv("data/CICs.csv")
```
4. Generate new inactive compounds: use the `generate.py` script to generate additional inactive compounds
```bash
python scripts/generate.py --adu ?????????????????
```

## Usage
This repo provides:
- Pre-processed datasets of CICs and GICs for predictive model development.
- Scripts to generate additional GICs using a trained generative AI model.

## Citation
- If you use InertDB in your research, please considering citing the following publication:
```
@article{An2024,
    author    = {An et al.},
    title     = {InertDB: A Comprehensive Database of Biologically Inactive Compounds},
    doi       = {10.xxxx},
    journal   = {xxx}
    year      = {2024},
    volume    = {x},
    pages     = {x--x},
}
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/ann081993/InertDB/blob/main/LICENSE) for details.

