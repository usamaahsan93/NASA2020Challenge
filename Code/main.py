#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:25:05 2020

@author: usama
"""

import numpy as np
# from sklearn.decomposition import PCA
# from sklearn.feature_selection import VarianceThreshold



# Workplaces closures / Cancellation of public events / Restrictions on public gatherings / Stay-at-home restrictions / Restrictions on internal movement / International travel controls we can do these ones first


import warnings
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

warnings.filterwarnings("ignore")
plt.close('all')

fileName='Italy'
df=pd.read_csv(fileName+'.csv')
dates=df['date']
dates=np.array(dates)

df=df.drop(columns=['Date_repor','Country','WHO_region','date','tests_units'])
scaling=MinMaxScaler()
_scaled=scaling.fit_transform(df)
dfScaled = pd.DataFrame(_scaled, columns=df.columns,index=df.index)

plt.plot(dfScaled['total_cases'],'*',label='Total Cases')
plt.plot(dfScaled['Close public transport (OxBSG)'],'o',label='Public Transport')
plt.plot(dfScaled['International travel controls (OxBSG)'],'h',label='International Travel Controls')


plt.plot(dfScaled['Workplace Closures (OxBSG)'],'s',label='Workplace Closures')
plt.plot(dfScaled['Cancel public events (OxBSG)'],'1',label='Cancel public events')

plt.plot(dfScaled['Restrictions on gatherings (OxBSG)'],'d',label='Restrictions on gatherings')
plt.plot(dfScaled['Stay at home requirements (OxBSG)'],'D',label='Stay at home requirements')

plt.plot(dfScaled['Restrictions on internal movement (OxBSG)'],'x',label='Restrictions on internal movement')

xx=np.arange(0,120,10)
xDates=dates[xx]
plt.xticks(xx,xDates,rotation=30)


plt.xlabel('Time',fontsize=14)
plt.title(fileName,fontsize=18)
plt.legend()
plt.grid()