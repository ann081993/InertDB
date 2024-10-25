# InertDB:
A Comprehensive Database of Biologically Inactive Compounds

<p align="center">
  <img src="/GA.png" width="75%" height="75%" title="InertDB-overview">
</p>

## Overview
InertDB
- Aims to enhance the robustness and accuracy of machine learning models in toxicology and pharmacology
- Offers a comprehensive resource for biologically inactive small molecules
- Provides inactive compounds curated curated from [PubChem](https://pubchem.ncbi.nlm.nih.gov/)

## Inactive compounds
- **Curated Inactive Compounds** (`CICs`): 3,205 compounds identified as inactive from the PubChem database after extensive curation and analysis of bioassay results.
- **Generated Inactive Compounds** (`GICs`): 64,368 potential inactive compounds generated using deep generative AI, trained on the CICs to expand the chemical space.

## Download
```sh
wget https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_cics.txt
wget https://raw.githubusercontent.com/ann081993/InertDB/main/data/inertdb_gics.txt
```

## Key applications
- Predictive Modeling: Enhance the performance of machine learning models in predicting biological activity by incorporating reliable inactive compounds from InertDB.
- Virtual Screening: Use InertDB as an extensive library for virtual screening to identify pharmacologically active compounds while minimizing the risk of off-target effects.

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

