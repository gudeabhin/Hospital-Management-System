#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:58:15 2021

@author: abhingude
"""

import pandas as pd
import random
hid=[]
rating=[]
df=pd.read_csv("hospital.csv")
for i in range(len(df)):
    hid.append(i+1)
    k=random.randint(0,5)
    rating.append(k)
df['hid']=hid
df['rating']=rating
df.to_csv("hospital.csv")

