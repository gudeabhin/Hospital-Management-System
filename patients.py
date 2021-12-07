#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 17:42:15 2021

@author: abhingude
"""

import pandas as pd
import random


hosp=pd.read_csv("hospital.csv")
states=list(set(hosp['state']))

pid=[]
state=[]
dob=[]
ins=[]

df=pd.read_csv("patients.csv")
for i in range(len(df)):
    pid.append(i+1)
    
    s=random.randint(0,(len(states)-1))
    state.append(states[s])
    
    month=random.randint(1,12)
    day=random.randint(1,30)
    year=random.randint(1939,2005)
    dob_doc=str(month)+"/"+str(day)+"/"+str(year)
    #datetime_object = datetime.strptime(dob_doc, '%m/%d/%Y').date()
    dob.append(dob_doc)
    
    i=random.randint(0,1)
    if(i==0):
        ins.append(True)
    else:
        ins.append(False)
        
df['pid']=pid
df['state']=state
df['dob']=dob
df['insurance']=ins
df.to_csv("patients.csv")