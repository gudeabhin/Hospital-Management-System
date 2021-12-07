#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:45:21 2021

@author: abhingude
"""

import pandas as pd
import random

r_id=[]
med_id=[]

for i in range(7500):
    r=random.randint(1,1500)
    med=random.randint(1,328)
    r_id.append(r)
    med_id.append(med)

df=pd.DataFrame()
df['r_id']=r_id
df['med_id']=med_id

df.to_csv("reports_has_medicines.csv")