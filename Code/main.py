#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:25:05 2020

@author: usama
"""

# import numpy as np
# from sklearn.decomposition import PCA
# from sklearn.feature_selection import VarianceThreshold
import warnings
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

warnings.filterwarnings("ignore")
plt.close('all')

fileName='China'
df=pd.read_csv(fileName+'.csv')
df=df.drop(columns=['Date_repor','Country','WHO_region','date','tests_units'])
scaling=MinMaxScaler()
_scaled=scaling.fit_transform(df)
dfScaled = pd.DataFrame(_scaled, columns=df.columns,index=df.index)

# dfRatio=df[['Cumulative_deaths','population_density','Government Response Stringency Index ((0 to 100, 100 = strictest))']]
# date=df['Date_repor']
# y=dfRatio['Cumulative_deaths']/dfRatio['population_density']

# plt.t(y,label='Cummulative Deaths / Population Density')
# plt.ploplot(dfRatio['Cumulative_deaths'],'o-.',label='Cummulative Deaths')
# plt.plot(dfRatio['Cumulative_deaths']/4645,'o-.',label='Cummulative Deaths (Normalized)')
# plt.plot(dfRatio['Government Response Stringency Index ((0 to 100, 100 = strictest))']/100,label='Govt. Response')
# plt.scatter(dfRatio['Cumulative_deaths'],dfRatio['Government Response Stringency Index ((0 to 100, 100 = strictest))'])
# plt.xlabel('Cummulative Deaths')
# plt.ylabel('Govt. Response')
# plt.plot(dfRatio['Cumulative_deaths']/4645,label='Cumm. Deaths')

plt.plot(dfScaled['total_cases'],label='Total Cases')
plt.plot(dfScaled['Close public transport (OxBSG)'],label='Public Transport')
plt.plot(dfScaled['International travel controls (OxBSG)'],label='International Travel Controls')

plt.xlabel('Time',fontsize=14)
plt.title(fileName,fontsize=18)
plt.legend()
plt.grid()