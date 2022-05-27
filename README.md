# Novel Diagnostic Model in Rheumatoid Arthritis 
Collabrated with **Peking University People's Hospital**, we built diagnostic model for Rheumatoid Arthritis (RA) based on protein array.
With 44 selected autoantibodies as markers, the model has achieved high accuracy (AUC=0.86, Specificity=0.9, Sensitivity=0.68).
Here, we provided the model and script for RA prediction.

## Dependencies
- python3
- numpy
- sklearn
- pickle
- pandas

## Usage
``git clone https://github.com/gao-lab/RA_prediction.git``

``python RA_prediction.py example.txt output.txt``

*Both input file and output file are **REQUIRED**.

## Input
See **example.txt**. The first row is the patient IDs and should be started with "#". 
The first column is the IDs of the autoantibody markers (**RFE.select.ids**).
Note that the autoantibody expression value in protein array shoulde be with the same rank with **RFE.select.ids**.

## Contact
Yu-Jian Kang <<kangyj@mail.cbi.pku.edu.cn>>
