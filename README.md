# InertDB: A Comprehensive Database of Biologically Inactive Compounds

<img src="/GA.png" width="40%" height="40%" title="InertDB"></img>

### Overview
InertDB is a curated database designed to serve as a comprehensive resource for biologically inactive small molecules. This database can be utilized in AI-assisted drug discovery and predictive modeling, providing a unique collection of compounds identified as inactive across diverse bioassays from PubChem. InertDB aims to enhance the robustness and accuracy of machine learning models in toxicology and pharmacology by offering a reliable set of inactive compounds.

### Inactive compounds
- Curated Inactive Compounds (`CICs`): 3,205 compounds identified as inactive from the PubChem database after extensive curation and analysis of bioassay results.
- Generated Inactive Compounds (`GICs`): 64,368 potential inactive compounds generated using deep generative AI, trained on the CICs to expand the chemical space.
- Bioassay Diversity Metrics: Implementation of novel metrics like Dassay and Nassay to evaluate the diversity of bioassays, ensuring a comprehensive selection of inactive compounds.

### Key applications
1. Virtual Screening: Use InertDB as an extensive library for virtual screening to identify pharmacologically active compounds while minimizing the risk of off-target effects.
2. Predictive Modeling: Enhance the performance of machine learning models in predicting biological activity by incorporating reliable inactive compounds from InertDB.
3. Chemical Space Exploration: Analyze the unique chemical space of inactive compounds, contributing to a better understanding of structure-activity relationships.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Please cite:
- If you use InertDB in your research, please considering citing our paper:
Seungchan An et al., InertDB as a Resource of Biologically Inactive Small Molecules
