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

   
def plot(dates,data,l,countryName):
    plt.close('all')
    plt.figure()

    mrkr=['H','o','1','4','*','h','2','+','3','x']
    total=len(l)
    c=0
    
    for i in l:
        plt.plot(data[i], label=i,marker=mrkr[c%total],linestyle='')
        c=c+1
        
    xx=np.arange(0,120,10)
    xDates=dates[xx]
    plt.xticks(xx,xDates,rotation=30)
    plt.xlabel('Time',fontsize=14)
    plt.title(chosen_country,fontsize=18)
    plt.legend()
    plt.grid()

def dataScaling(df):
    scaling=MinMaxScaler()
    _scaled=scaling.fit_transform(df)
    dfScaled = pd.DataFrame(_scaled, columns=df.columns,index=df.index)
    return dfScaled


def load_and_format_Data(fname):
    df=pd.read_csv(chosen_country+'.csv')
    dates=df['date']
    dates=np.array(dates)
    
    df=df.drop(columns=['Date_repor','Country','WHO_region','date','tests_units'])
     
    return df,dates


if __name__ == '__main__':
    #Dataset file name
    chosen_country='Italy'
    
    #Data format and object data removed, and dates extracted seperately
    df,dates=load_and_format_Data(chosen_country)
    dfScaled=dataScaling(df)
    
    #User will enter this list using checklist and plot will be adjusted accordingly
    l=['total_cases','Close public transport (OxBSG)',
       'International travel controls (OxBSG)','Workplace Closures (OxBSG)',
       'Cancel public events (OxBSG)', 'Restrictions on gatherings (OxBSG)',
       'Stay at home requirements (OxBSG)','Restrictions on internal movement (OxBSG)'
       ]
    
    plot(dates,dfScaled,l,chosen_country)
