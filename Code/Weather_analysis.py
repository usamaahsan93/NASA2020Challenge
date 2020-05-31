#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 03:01:35 2020

@author: usama
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
df1=pd.read_csv('BeijingDegreeC.csv')
df2=pd.read_csv('./Datasets/China.csv')


cases=df2['total_cases']

# plt.plot(cases)
# plt.plot(df1)


fig,ax = plt.subplots()
# make a plot
ax.plot(cases, color="red", marker="o")
# set x-axis label
# ax.set_xlabel("year",fontsize=14)
# set y-axis label
ax.set_ylabel("Total Cases",color="red",fontsize=14)

ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(df1,color="blue",marker="o")
ax2.set_ylabel("$\degree C$",color="blue",fontsize=14)
plt.show()
plt.grid()
plt.title('China')

#############################################################
df1=pd.read_csv('ItalyDegreeC.csv')
df2=pd.read_csv('./Datasets/Italy.csv')


cases=df2['total_cases']

# plt.plot(cases)
# plt.plot(df1)


fig,ax = plt.subplots()
# make a plot
ax.plot(cases, color="red", marker="o")
# set x-axis label
# ax.set_xlabel("year",fontsize=14)
# set y-axis label
ax.set_ylabel("Total Cases",color="red",fontsize=14)

ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(df1,color="blue",marker="o")
ax2.set_ylabel("$\degree C$",color="blue",fontsize=14)
plt.show()
plt.grid()
plt.title('Italy')









