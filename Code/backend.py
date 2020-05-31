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
# plt.close('all')

# chosen_country='Italy'
# df=pd.read_csv(chosen_country+'.csv')
# dates=df['date']
# dates=np.array(dates)

# df=df.drop(columns=['Date_repor','Country','WHO_region','date','tests_units'])
# scaling=MinMaxScaler()
# _scaled=scaling.fit_transform(df)
# dfScaled = pd.DataFrame(_scaled, columns=df.columns,index=df.index)

# plt.plot(dfScaled['total_cases'],'*',label='Total Cases')
# plt.plot(dfScaled['Close public transport (OxBSG)'],'o',label='Public Transport')
# plt.plot(dfScaled['International travel controls (OxBSG)'],'h',label='International Travel Controls')


# plt.plot(dfScaled['Workplace Closures (OxBSG)'],'s',label='Workplace Closures')
# plt.plot(dfScaled['Cancel public events (OxBSG)'],'1',label='Cancel public events')

# plt.plot(dfScaled['Restrictions on gatherings (OxBSG)'],'d',label='Restrictions on gatherings')
# plt.plot(dfScaled['Stay at home requirements (OxBSG)'],'D',label='Stay at home requirements')

# plt.plot(dfScaled['Restrictions on internal movement (OxBSG)'],'x',label='Restrictions on internal movement')

# xx=np.arange(0,120,10)
# xDates=dates[xx]
# plt.xticks(xx,xDates,rotation=30)


# plt.xlabel('Time',fontsize=14)
# plt.title(chosen_country,fontsize=18)
# plt.legend()
# plt.grid()

   
def plot(dates,data,l,countryName):
    plt.close('all')

    plt.figure()
    # cases_figure = plt.Figure(figsize=(10, 10), dpi=100)
    # cases_axis = cases_figure.add_subplot(111)

    mrkr=['H','o','1','4','*','h','2','+','3','x']
    total=len(l)
    c=0
    
    for i in l:
        plt.plot(data[i], label=i,marker=mrkr[c%total],linestyle='')
        c=c+1
        
    xx=np.arange(0,120,10)
    xDates=dates[xx]
    plt.xticks(xx,xDates,rotation=30)
    # cases_axis.set_xticks(xx,dates)#,rotation=30)
    # for tick in cases_axis.get_xticklabels():
        # tick.set_rotation(45)


    
    # cases_axis.set_
    xx=np.arange(0,120,10)
    plt.xlabel('Time',fontsize=14)
    plt.title(chosen_country,fontsize=18)
    plt.legend()
    plt.grid()

# def plott(dates,data,l,countryName):
#     plt.close('all')
#     # plt.figure()
#     cases_figure = plt.Figure(figsize=(10, 10), dpi=100)
#     cases_axis = cases_figure.add_subplot(111)

#     mrkr=['H','o','1','4','*','h','2','+','3','x']
#     total=len(l)
#     c=0
#     i='total_cases'
#     cases_axis.plot(data[i], label=i,marker=mrkr[c%total],linestyle='')
#     cases_figure.show()
#     1/0
#     for i in l:
#         cases_axis.plot(data[i], label=i,marker=mrkr[c%total],linestyle='')
#         # cases_axis.show()
#         1/0
#         c=c+1
        
#     # xx=np.arange(0,120,10)
#     # xDates=dates[xx]
#     # plt.xticks(xx,xDates,rotation=30)
    
#     # cases_axis.set_xticks(xx,dates)#,rotation=30)
#     # for tick in cases_axis.get_xticklabels():
#         # tick.set_rotation(45)


    
#     # cases_axis.set_
#     # xx=np.arange(0,120,10)
#     # plt.xlabel('Time',fontsize=14)
#     # plt.title(chosen_country,fontsize=18)
#     # plt.legend()
#     # plt.grid()

    
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
    
    chosen_country='Italy'
    df,dates=load_and_format_Data(chosen_country)
    # df=pd.read_csv(chosen_country+'.csv')
    # dates=df['date']
    # dates=np.array(dates)
    
    # df=df.drop(columns=['Date_repor','Country','WHO_region','date','tests_units'])
    # # scaling=MinMaxScaler()
    # _scaled=scaling.fit_transform(df)
    # dfScaled = pd.DataFrame(_scaled, columns=df.columns,index=df.index)
    dfScaled=dataScaling(df)
    
    
    l=['total_cases','Close public transport (OxBSG)',
       'International travel controls (OxBSG)','Workplace Closures (OxBSG)',
       'Cancel public events (OxBSG)', 'Restrictions on gatherings (OxBSG)',
       'Stay at home requirements (OxBSG)','Restrictions on internal movement (OxBSG)'
       ]
    
    # plot(dates,dfScaled,l,chosen_country)
    plot(dates,dfScaled,l,chosen_country)
    
    # 1/0
    
    # l=['total_cases','Close public transport (OxBSG)',
    #     'Restrictions on internal movement (OxBSG)'
    #     ]
    # skip=input('Paused.. Press any key to continue')
    # plot(dates,dfScaled,l,chosen_country)
    # cases_axis.plot(df_scaled[i], label=i)