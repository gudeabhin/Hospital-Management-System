#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:28:09 2021

@author: abhingude
"""

import pandas as pd
import random

t_id=[]
hid=[]
amount=[]
pid=[]
date1=[]


doc=pd.read_csv("doctors.csv")
appt=pd.read_csv("appointments.csv")

for i in range(len(appt)):
    t=appt.iloc[i]['a_id']
    t_id.append(t)
    
    p=appt.iloc[i]['pid']
    pid.append(p)
    
    am=random.randint(400,25000)
    amount.append(am)
    
    d=appt.iloc[i]['appt_date']
    date1.append(d)
    
    dctr=appt.iloc[i]['d_id']
    h=doc.iloc[dctr-1]['hid']
    #print(h)
    hid.append(h)
    
df=pd.DataFrame()
df['t_id']=t_id
df['hid']=hid
df['pid']=pid
df['amount']=amount
df['date']=date1

df.to_csv("payments.csv")