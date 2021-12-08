#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:07:45 2021

@author: abhingude
"""

import pandas as pd
import random

a_id=[]
appt_date=[]
r_id=[]
pid=[]
d_id=[]

for i in range(1500):
    a_id.append(i+1)
    
    month=random.randint(1,12)
    day=random.randint(1,30)
    year=random.randint(2020,2021)
    dob_doc=str(month)+"/"+str(day)+"/"+str(year)
    #datetime_object = datetime.strptime(dob_doc, '%m/%d/%Y').date()
    appt_date.append(dob_doc)
    
    r_id.append(i+1)
    
    p=random.randint(1,3003)
    pid.append(p)
    
    d=random.randint(1,6782)
    d_id.append(d)
    
df=pd.DataFrame()
df['a_id']=a_id
df['appt_date']=appt_date
df['r_id']=r_id
df['pid']=pid
df['d_id']=d_id

df.to_csv("appointments.csv")