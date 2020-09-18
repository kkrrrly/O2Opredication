import os,sys,pickle

import numpy as np
import pandas as pd  

data_offline = pd.read_csv('./data/ccf_offline_stage1_train.csv')
data_online = pd.read_csv('./data/ccf_online_stage1_train.csv')
data_test = pd.read_csv('./data/ccf_offline_stage1_test_revised.csv')

print(data_offline)
