#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:34:56 2021

@author: abhingude
"""

import pandas as pd
import random
from datetime import datetime

degree=["MS","MD","DM","MBBS","FRCS","Super Speciality"]

doc_id=[]
hid=[]
dob=[]
deg=[]
suc_rate=[]
exp=[]
dept=[]

df=pd.read_csv("doctors.csv")

for i in range(1500):
    doc_id.append(i+1)
    
    month=random.randint(1,12)
    day=random.randint(1,30)
    year=random.randint(1939,2005)
    dob_doc=str(month)+"/"+str(day)+"/"+str(year)
    #datetime_object = datetime.strptime(dob_doc, '%m/%d/%Y').date()
    dob.append(dob_doc)
    
    d=random.randint(0,5)
    de=degree[d]
    deg.append(de)
    
    s=random.randint(65,100)
    suc_rate.append(s)
    
    e=2021-year
    exp.append(e)

    hid.append(i+1)
    
    dep=random.randint(1,20)
    dept.append(dep)
    

for i in range(1500,len(df)):
    doc_id.append(i+1)
    
    month=random.randint(1,12)
    day=random.randint(1,30)
    year=random.randint(1939,2005)
    dob_doc=str(month)+"/"+str(day)+"/"+str(year)
    #datetime_object = datetime.strptime(dob_doc, '%m/%d/%Y').date()
    dob.append(dob_doc)
    
    d=random.randint(0,5)
    de=degree[d]
    deg.append(de)
    
    s=random.randint(65,100)
    suc_rate.append(s)
    
    e=2021-year
    exp.append(e)
    
    h=random.randint(1,1500)
    hid.append(h)
    
    dep=random.randint(1,20)
    dept.append(dep)
    


df['doc_id']=doc_id
df['dob']=dob
df['degree']=deg
df['success_rate']=suc_rate
df['experience']=exp
df['hid']=hid
df['dep_id']=dept
    
df.to_csv("doctors.csv")
