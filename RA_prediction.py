#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Copyright (c) 2022 Yu-Jian Kang, Created on 2022-05-26 15:24:23.

Purpose Description
-----------------------
    Rheumatoid Arthritis prediction with autoantibodies

Contact
---------------
    Yu-Jian Kang <kangyj@mail.cbi.pku.edu.cn>

Example
-------
    python RA_prediction.py input_file output_file

"""

#================== Source Code ==================

import sys
if len(sys.argv) < 3:
    sys.stderr.write(__doc__)
    sys.exit(1)


import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# load data
sys.stderr.write("[INFO] import data ...\n")

X = []
varname = []
file_in = open(sys.argv[1],'r')
for line in file_in:
    arr = line.rstrip("\n").split("\t")
    if line.startswith("#"):
        sample_list = arr[1:]
        continue
    data_line = np.float64(arr[1:])
    X.append(np.log2(data_line+1)) # transform expression abundance to log2(x+1)
file_in.close()


# scale data
sys.stderr.write("[INFO] scale data ...\n")

Xt = np.asarray(np.transpose(X))
with open('data_scaler.pkl', 'rb') as my_scaler:
    scaler = pickle.load(my_scaler)
my_scaler.close()
Xtscale = scaler.transform(Xt)


# load model
sys.stderr.write("[INFO] prediction ...\n")

with open('RA_model.pkl', 'rb') as my_model:
    classifier = pickle.load(my_model)
my_model.close()
probas = classifier.predict_proba(Xtscale)

# output data
sys.stderr.write("[INFO] write output ...\n")
threshold = 0.635 # control specificity to 0.9
labels = np.where(probas[:,1] > threshold, 1, 0)
data = {'#Sample':sample_list, 'Probability':probas[:,1], 'Label':labels}
df = pd.DataFrame(data)
df.to_csv(sys.argv[2], index = False, sep='\t')

sys.stderr.write("[INFO] done ...\n")
