#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:04:04 2021

@author: abhingude
"""

import pandas as pd
import random
from datetime import datetime

a_id=[]
vehicle_no=[]
vehicle_type=[]
hid=[]

df=pd.DataFrame()


alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
type1=['car','van','big van']

for i in range(200):
    a_id.append(i+1)
    
    
    fl=random.randint(0,25)
    ll=random.randint(0,25)
    n=random.randint(500,1000)
    veh_num=alpha[fl]+alpha[ll]+str(n)
    vehicle_no.append(veh_num)
    
    
    t=random.randint(0,2)
    vehicle_type.append(type1[t])
    
    h=random.randint(1,7292)
    hid.append(h)


df['a_id']=a_id
df['vehicle_no']=vehicle_no
df['vehicle_type']=vehicle_type
df['hid']=hid
df.to_csv("ambulance.csv")