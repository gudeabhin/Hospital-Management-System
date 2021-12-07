#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:00:05 2021

@author: abhingude
"""

import pandas as pd
import random

med_id=[]
price_per_unit=[]

df=pd.read_csv("medicines.csv")


for i in range(len(df)):
    med_id.append(i+1)
    
    p=df.iloc[i]['price_per_unit']
    d=p.split()[0]
    s=d[:(len(d)-1)]
    cur=d[len(d)-1:]
    if(cur=='¢'):
        s=float(s)/100
    price_per_unit.append(s)
    
df['med_id']=med_id
df['price_per_unit']=price_per_unit

df.to_csv("medicines.csv")
    