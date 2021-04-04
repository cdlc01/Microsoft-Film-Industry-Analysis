df#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:56:48 2021

@author: george
"""
from matplotlib import pyplot as plt
DF.description()
rows_with_na=DF.apply(lambda c:c.isna().sum(),axis=1).value_counts()
na_by_columns=DF.apply(lambda c:c.isna().sum(),axis=0)
dep_variable='total_gross'

attr='story'
data=DF.copy()
data=data.dropna(subset=[attr])
obs=data.shape[0]
data['lengths']=data[attr].apply(lambda p:len(p.split(' ')))
len_descr=lengths.describe()
data.plot(x='lengths',
          y=dep_variable,
          kind='scatter'
          )


attr='premier_date'
data=DF.copy()
data=data.dropna(subset=[attr])
obs=data.shape[0]
data['Q']=data[attr].apply(lambda date:date.quarter)
quarter_desc=data.Q.value_counts()
rev_byQ=data.groupby(['Q'])[dep_variable].agg(['min','max','mean','median','std'])
data['M']=data[attr].apply(lambda date:date.month)
montly_desc=data.M.value_counts()
rev_byM=data.groupby(['M'])[dep_variable].agg(['min','max','mean','median','std'])



attr='genres'
data=DF.copy()
data=data.dropna(subset=[attr])
obs=data.shape[0]
data['genre']=data.genres.apply(lambda l:' x '.join(l))
#most_frequent=data['genre'].value_counts().nlargest(10)
splits=data.groupby('genre')[dep_variable].agg(['count','mean','median','std'])
most_revenue=splits.nlargest(10,'mean')[['count','mean']]
most_frequent=splits.nlargest(10,'count')

attr='runtimes'
data=DF.copy()
data=data.dropna(subset=[attr])
obs=data.shape[0]
ax=data.plot(x='runtimes',y=dep_variable,kind='scatter',
          xlabel='Runtime (Minutes)',
          ylabel='Gross Revenue',
          title='Comparing Runtimes to Total Revenue')

attr='Rating_US'
data=DF.copy()
data=data.dropna(subset=[attr])
obs=data.shape[0]
descr=data[attr].value_counts()
splits=data.groupby(attr)[dep_variable].agg(['count','mean','median','std'])


attr='votes'
data=DF.copy()
data=data.dropna(subset=[attr])
obs=data.shape[0]
data['product']=data['votes']*data['rating']
data_neg=data[data.rating<5.0]
data_pos=data[data.rating>7.0]
data_pos.plot(x=attr,y=dep_variable,kind='scatter')
data_neg.plot(x=attr,y=dep_variable,kind='scatter')


data=DF.copy()
data['genre']=data.genres.apply(lambda l:' x '.join(l))
data=data.dropna(subset=[attr])
obs=data.shape[0]
data['genre']=data.genres.apply(lambda l:' x '.join(l))
attr='genres'
data=data.dropna(subset=[attr])
obs=data.shape[0]
data['genre']=data.genres.apply(lambda l:' x '.join(l))
attr='Rating_US'
data=data.dropna(subset=[attr])
pd.crosstab(data.genre,data.Rating_US,margins=True)
_.drop('All',axis=0)
_.nlargest(10,columns='All')

def get_genre_specific(DF,genre):
    genre_only_DF=DF.genres.apply(lambda l:genre in l)