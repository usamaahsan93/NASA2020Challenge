#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:25:05 2020

@author: usama
"""

import numpy as np
import warnings
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

warnings.filterwarnings("ignore")

   
def plot(dates,data,l,countryName,analysisType,baseline=True,factor=1):
    plt.figure(figsize=(11,6.875))

    if baseline:
        a=data['Cumulative_cases'].to_numpy()
        z=[x - a[i - 1] for i, x in enumerate(a)][1:]
        z=z/max(z)
        z=z*factor
        plt.plot(z,label='Difference of consecutive Cummulative Cases',c='r')

    mrkr=['H','o','1','4','*','h','2','+','3','x']
    total=len(l)
    c=0
    
    for i in l:
        plt.plot(data[i], label=i,marker=mrkr[c%total],linestyle='')
        c=c+1
        
    xx=np.arange(0,len(dates),10)
    xDates=dates[xx]
    plt.xticks(xx,xDates,rotation=30)
    plt.xlabel('Time',fontsize=14)
    plt.title(countryName+' - '+analysisType,fontsize=18)
    plt.legend()
    plt.grid()

def dataScaling(df):
    scaling=MinMaxScaler()
    _scaled=scaling.fit_transform(df)
    dfScaled = pd.DataFrame(_scaled, columns=df.columns,index=df.index)
    return dfScaled


def load_and_format_Data(fname):
    df=pd.read_csv(fname+'.csv')
    dates=df['date']
    dates=np.array(dates)
    
    df=df.drop(columns=['Country','WHO_region','date','tests_units'])
     
    return df,dates





#######################################################################
####################### GARBAGE CODE ##################################
#######################################################################


# if __name__ == '__main__':
#     plt.close('all')
#     #Dataset file name
#     chosen_country='Sweden'
    
#     #Data format and object data removed, and dates extracted seperately
#     df,dates=load_and_format_Data(chosen_country)
#     dfScaled=dataScaling(df)
    
#     #User will enter this list using checklist and plot will be adjusted accordingly
#     l=['total_cases','Close public transport (OxBSG)',
#        'International travel controls (OxBSG)','Workplace Closures (OxBSG)',
#        'Cancel public events (OxBSG)', 'Restrictions on gatherings (OxBSG)',
#        'Stay at home requirements (OxBSG)','Restrictions on internal movement (OxBSG)'
#        ]
    
#     l=[
#        'International travel controls (OxBSG)',
#        'Restrictions on internal movement (OxBSG)'
       
#        ]    
#     plot(dates,dfScaled,l,chosen_country,analysisType='Travel ban',baseline=True,factor=4)


#     l=[
#        'School closures',
#        'Workplace Closures (OxBSG)'       
#        ]
#     plot(dates,dfScaled,l,chosen_country,analysisType='Closure policies',baseline=True,factor=4)

#     l=[
#        'Stay at home requirements (OxBSG)',
#        'Cancel public events (OxBSG)'       
#        ]
#     plot(dates,dfScaled,l,chosen_country,analysisType='Isolation policies',baseline=True,factor=4)

#     # l=[
#     #    'gdp_per_capita',
#     #    'extreme_poverty'       
#     #    ]
#     # plot(dates,dfScaled,l,chosen_country,analysisType='Average economical condition',baseline=True)


#     l=[
#        'Testing policy (OxBSG)',
#        'Contact tracing (OxBSG)'       
#        ]
#     plot(dates,dfScaled,l,chosen_country,analysisType='Tracing and testing policy',baseline=True,factor=4)














# a=df['Cumulative_cases'].to_numpy()
# z=[x - a[i - 1] for i, x in enumerate(a)][1:]
# z=z/max(z)
# # z=MinMaxScaler().fit(z)
# plt.plot(z,label='Difference of consecutive Cummulative Cases',c='r')
# plt.legend()
# plt.yscale('log')