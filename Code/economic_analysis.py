#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 23:52:26 2020

@author: usama
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from backend import load_and_format_Data

import os

plt.close('all')

path='./Datasets'
arr = os.listdir(path)


dataframes=[]
dates=[]

for i in arr:
    df=pd.read_csv(path+'/'+i)
    date=df['date']
    date=np.array(date)
    
    df=df.drop(columns=['Country','WHO_region','date','tests_units'])
    dataframes.append(df)
    dates.append(date)

# 1/0
popDensity=[]
gdp=[]
cumCases=[]
population=[]
for i in dataframes:
    popDensity.append(max(i['population_density']))
    gdp.append(max(i['gdp_per_capita']))
    population.append(max(i['population']))
    cumCases.append(max(i['Cumulative_cases']))



l=[popDensity,gdp,population]
graphs=['Population Density','GDP','Population']

numOfGraphs=0
length=11
height=0.625*length


for i in l:
    plt.figure(figsize=(length, height))
    plt.scatter(i,cumCases)
    plt.xlabel(graphs[numOfGraphs],fontsize=16)
    plt.ylabel('Cumulative Cases',fontsize=16)
    plt.yscale('log')
    
    plt.grid()
    
    for j in range(len(arr)):
        country=arr[j]
        plt.annotate(s=country[:-4],xy=(i[j],cumCases[j]))#,rotation=-10)
    
    plt.savefig('./Graphs/'+graphs[numOfGraphs],quality=100)
    numOfGraphs=numOfGraphs+1
    
        # 1/0
    # 1/0
    