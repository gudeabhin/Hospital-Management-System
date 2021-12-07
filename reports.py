#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:29:49 2021

@author: abhingude
"""

import pandas as pd
import random

sry=['Good','Doing Well','Alright','Need to checkup again' , 'consult another doctor' , 'lab scans needed' , 'Immediate Care Required', 'Shift to ICU' , 'Needs another surgery' ,
         'consult in 3 months']

r_id=[]
summary=[]
df=pd.DataFrame()
for i in range(1500):
    r_id.append(i+1)
    s=random.randint(0,9)
    sp=sry[s]
    summary.append(sp)
    
df['r_id']=r_id
df['summary']=summary

df.to_csv("reports.csv")