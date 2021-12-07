#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:42:07 2021

@author: abhingude
"""


import pandas as pd
import random
from datetime import datetime


s_id=[]
hid=[]
dob=[]
exp=[]
salary=[]
dept=[]

df=pd.read_csv("staff.csv")

for i in range(1500):
    s_id.append(i+1)
    
    month=random.randint(1,12)
    day=random.randint(1,30)
    year=random.randint(1939,2005)
    dob_doc=str(month)+"/"+str(day)+"/"+str(year)
    #datetime_object = datetime.strptime(dob_doc, '%m/%d/%Y').date()
    dob.append(dob_doc)
    
    
    e=2021-year
    exp.append(e)
    
    s=e*1500
    salary.append(s)

    hid.append(i+1)
    
    dep=random.randint(1,20)
    dept.append(dep)
    

for i in range(1500,len(df)):
    s_id.append(i+1)
    
    month=random.randint(1,12)
    day=random.randint(1,30)
    year=random.randint(1939,2005)
    dob_doc=str(month)+"/"+str(day)+"/"+str(year)
    #datetime_object = datetime.strptime(dob_doc, '%m/%d/%Y').date()
    dob.append(dob_doc)
    
    
    e=2021-year
    exp.append(e)
    
    s=e*1500
    salary.append(s)

    
    h=random.randint(1,1500)
    hid.append(h)
    
    dep=random.randint(1,20)
    dept.append(dep)
    


df['s_id']=s_id
df['dob']=dob
df['experience']=exp
df['salary']=salary
df['hid']=hid
df['dep_id']=dept
    
df.to_csv("staff.csv")
