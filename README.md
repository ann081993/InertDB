# InertDB: A Comprehensive Database of Biologically Inactive Compounds

<p align="center">
  <img src="/GA.png" width="75%" height="75%" title="InertDB-overview">
</p>

## Overview
InertDB
- Is a curated database designed to serve as a comprehensive resource for biologically inactive small molecules
- Provides a unique collection of compounds identified as inactive across diverse bioassays from PubChem
- Can be utilized in AI-assisted drug discovery and predictive modeling
- Aims to enhance the robustness and accuracy of machine learning models in toxicology and pharmacology by offering a reliable set of inactive compounds

## Inactive compounds
- **Curated Inactive Compounds** (`CICs`): 3,205 compounds identified as inactive from the PubChem database after extensive curation and analysis of bioassay results.
- **Generated Inactive Compounds** (`GICs`): 64,368 potential inactive compounds generated using deep generative AI, trained on the CICs to expand the chemical space.
- Bioassay Diversity Metrics: Implementation of novel metrics like Dassay and Nassay to evaluate the diversity of bioassays, ensuring a comprehensive selection of inactive compounds.

## Download
```sh
wget https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_cics.txt
wget https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_gics.txt
```

## Key applications
- Virtual Screening: Use InertDB as an extensive library for virtual screening to identify pharmacologically active compounds while minimizing the risk of off-target effects.
- Predictive Modeling: Enhance the performance of machine learning models in predicting biological activity by incorporating reliable inactive compounds from InertDB.
- Chemical Space Exploration: Analyze the unique chemical space of inactive compounds, contributing to a better understanding of structure-activity relationships.

## Please cite:
- If you use InertDB in your research, please considering citing the following publication:
```
@article{An2024,
    author    = {An et al.,},
    title     = {InertDB: A Comprehensive Database of Biologically Inactive Compounds},
    doi       = {10.xxxx},
    journal   = {xxx}
    year      = {2024},
    volume    = {x},
    pages     = {x--x},
}
```

## License
This project is licensed under the MIT License.
