# SSB EIS Data Manager and ML Modeling
battery performance diagnose and prediction by distribution of relaxation times analysis and machine learning

This is a tool designed for managing and analyzing cycling and EIS (Electrochemical Impedance Spectroscopy) test data from commercial solid-state batteries (SSBs), i.e. the TDK Ceracharge cell. It supports the parsing of `.mpr` files exported from **Biologic** testing systems, and organizes the extracted data into a structured database. Furthermore, the tool incorporates machine learning (ML) models to diagnose and predict relative capacity based on historical performance data.

## Key Features

-  Automatic parsing of `.mpr` files (Biologic format)
-  Extraction and processing of cycling and EIS data
-  Local or remote database support for managing battery test history
-  ML models for performance diagnosis and prediction using EIS data

## Data Input and Output

### Input:

- Biologic `.mpr` files (including cycling and EIS test data)

### Output:

- Databases in SQL
- Visualization plots
- ML diagnosis and predictions 


## Acknowledgments
- Thanks to the github community for discussion, especially the authors of the proprietary Galvani
- Built with open-source tools including numpy, pandas, scikit-learn, galvani and matplotlib etc.
