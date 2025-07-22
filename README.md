# SSB EIS Data Manager and ML Modeling
## Battery performance diagnose and prediction by distribution of relaxation times analysis and machine learning

This is a tool designed for managing and analyzing cycling and EIS (Electrochemical Impedance Spectroscopy) test data from commercial solid-state batteries (SSBs), i.e., the TDK Ceracharge cell. It supports the parsing of `.mpr` files exported from **Biologic** testing systems, and organizes the extracted data into a structured database. Furthermore, the tool incorporates machine learning (ML) models to diagnose and predict relative capacity based on historical performance data.

## Key Features

-  Automatic parsing of `.mpr` files (Biologic format)
-  Extraction and processing of cycling and EIS data
-  Local or remote database support for managing battery test history
-  ML models for performance diagnosis and prediction using EIS data

## Data Input and Output

### Input:

- Biologic `.mpr` files (including cycling and EIS test data)
- path: /raw_data/...

### Output:

- Databases in SQL
- Visualization plots
- ML diagnosis and predictions

### Quick start without data processing
- run the 03 and 04 models using processed .csv files

## Acknowledgments
- Thanks to the github community for discussion, especially the authors of the proprietary Galvani
- Built with open-source tools including numpy, pandas, scikit-learn, galvani and matplotlib etc.

## Citation
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16313223.svg)](https://doi.org/10.5281/zenodo.16313223)

## License
- This project is licensed under the MIT License. See the LICENSE file for details.
