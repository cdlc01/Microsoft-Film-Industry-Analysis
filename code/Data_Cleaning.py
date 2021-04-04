#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:47:01 2021

@author: george
"""
import pandas as pd
import regex
def unpack_dict(key,series):
    new_series=sereis.apply(lambda x:x.get(key,np.nan))
    return new_series

def delim_nested_dict(d,key):
    try:
        s=d.get(key,np.nan)
    except:
        s=np.nan
    return s

def delim_nested_list(l,index):
    try:
        s=l[0:index]
    except:
        s=np.nan
    return s


def string_to_numb(s):
    n=int(s.replace(',','')) if(type(s)==str) else s
    return n


def clear_budgets(DF):
    DF_new=DF[DF['budget'].isna()==False]
    return DF_new

def USHK_Rating(certificate):
    s=', '.join(certificate)
    pattUS=r'United States:([A-Z\-0-9]{1,5})'
    pattHK=r'Hong Kong:([A-Z\-0-9]{1,5})'
    US_match=regex.search(pattUS,s)
    HK_match=regex.search(pattHK,s)
    US=US_match.groups()[0] if(US_match) else np.nan
    HK=HK_match.groups()[0] if(HK_match) else np.nan
    return US, HK
#Because some data''


DF.info()
DF_clean=DF.copy() #Start with a copy of original to avoid errors.
#First Rename our columns:
DF_clean=DF_clean.rename(columns={'plot outline':'story',
                         'language codes':'languages',
                         'production companies':'production',
                         'original air date':'release_date',
                         'country codes':'countries'
                         })
#Most obvious issue is with the runtimes which appear to be strings not lists.
DF_clean.runtimes.isna().sum() #notice we have 13 null values.
DF_clean[DF_clean.runtimes.isna()] #see that these are not particularly important.
DF_clean=DF_clean.dropna(subset=['runtimes'])
DF_clean.runtimes=DF_clean.runtimes.apply(lambda l:int(l[0]))
#We do not actually need the box_office column which stores data from IMDb that 
#is duplicative of data grabbed w/ box of mojo
DF_clean=DF_clean.drop(columns=['box office'])

#Through inspection of the year column, we see that there are some 
#entries which do not fit our criteria.  This is a little difficult 
#because the BOM data includes re-releases in their annual rankings.  
#To be safe, we drop all entries with yearss prior to 2009.
DF_clean=DF_clean[DF_clean.year>2009]

#Next, we want to get the string of release data into a timestamp data type. 
#notice a few entries does not have a release date.  Looked it up manually and reset
DF_clean.at['tt3735554','release_date']='08 Apr 2015'
DF_clean.at['tt2603600','release_date']='09 Oct 2016'
patt=r'([0-9]{0,2})[ ]*([A-Za-z]{3,4}) ([0-9]{4})'
groupings=DF_clean.release_date.str.extract(patt)
groupings[0]=groupings[0].replace('','01') #Fix another entry with a missing day.
DF_clean['release_date_str']=groupings[1]+' '+groupings[0]+' '+groupings[2]
func=lambda s:pd.to_datetime(s) if(type(s)==str) else s
DF_clean['premier_date']=DF_clean['release_date_str'].apply(func)
DF_clean=DF_clean.drop(columns=['release_date_str'])
###Next Wish to capture the certificates for US and HK
funcUS=lambda c:USHK_Rating(c)[0] if(type(c)==list) else c
funcHK=lambda c:USHK_Rating(c)[1] if(type(c)==list) else c
DF_clean['Rating_US']=DF_clean.certificates.apply(funcUS)
DF_clean['Rating_HK']=DF_clean.certificates.apply(funcHK)
#We drop the certificat`es column now that it is not needed
DF_clean=DF_clean.drop(columns=['certificates'])
#Last, but not least, we want to normalize our $ numbeers to improve readability
for key in ['budget','total_gross','intl_gross','domestic_gross']:
    DF_clean[key]=DF_clean[key]/1000000
#Save Out
DF_clean.to_pickle('/Users/george/Desktop/DataFrames/Final_Formatted.pkl')
