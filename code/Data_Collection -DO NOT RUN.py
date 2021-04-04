#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:46:29 2021

## FOR VIEWING ONLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## DO NO RUN THIS CODE UNDER ANY CIRCUMSTANCES!!!!!!!!!!!
## IT TOOK GEORGE'S COMPUTER AN ENTIRE DAY TO FINISH PULLING ALL
## THIS DATA OFF OF THE IMDB WEBSITE


##### DO
##### NOT
##### RUN
##### THIS
##### CODE

##### OMG OMG STOP DO NOT RUN ANY OF THE CODE BELOW

##### FOR VIEWING ONLY

@author: george
"""
#import os
#from imdb import IMDb
#import regex
#import pandas as pd
#import requests
#from bs4 import BeautifulSoup as bs
#import numpy as np
#import gzip
#from tqdm import tqdm
#import time
#import pickle
VARIABLES=['imdbID','year','genres','original air date',
           'plot outline','runtimes','title','cast',
           'country codes','director','language codes','production companies',
           'cast','rating','votes','certificates','box office'
           ]

def get_meta_data(folder_directory):
    meta_data=dict.fromkeys(os.listdir(folder_directory))
    meta_data
    for filename in os.listdir(folder_directory):
        try:
            with gzip.open(folder_directory+'/'+filename) as f:
                if filename.endswith('gz'):
                    df=pd.read_csv(f)
                else:
                    df=pd.read_csv(f,sep='\t')
                meta_data[filename]=(df.shape,df.columns)
        except:
            pass
    return meta_data

def collect_movie_objs_w_IDs(ids):
    ia=IMDb()
    movies={}
    errors=[]
    for x in tqdm(ids):   
        try:
            movie=ia.get_movie(x,info='main')
        except:
            errors.append(x)
        else:
            movies[x]=movie.data
        time.sleep(0.1)
    return movies,errors

def collect_movie_objs_with_titles(movies):
    errors=[]
    ia=IMDb()
    movie_objs={}
    for title,year in tqdm(movies.items()):
        try:
            matches=ia.search_movie(title,results=5)
        except:
            errors.append((title,0))
        if(len(matches)==1):
            movie=matches[0].movieID
        else:
            try:
                years=[m.data.get('year',0) for m in matches]
                if(year in years):
                    idx=years.index(year)
                else:
                    close=[abs(y-year) for y in years]
                    idx=close.index(min(close))
                movie=matches[idx].movieID
                pass
            except:
                errors.append((title,1))
        time.sleep(0.10)
        try:
            movie_objs[title]=ia.get_movie(movie,info='main').data
        except:
            errors.append((titles,2))
        time.sleep(0.10)
    return movie_objs,errors
def reduce_IMDb_Obj(data_obj):
    data_dict=data_obj.copy()
    x=data_dict.get('cast',False)
    if(x):
        top_bill=[c['name'] for c in x[0:5]]
        data_dict['cast']=top_bill
    else:
        pass
    x=data_dict.get('director',False)
    if(x):
        data_dict['director']=x[0]['name']
    else:
        pass
    x=data_dict.get('production companies',False)
    if(x):
        producers=[p['name'] for p in x]
        data_dict['production companies']=producers
    else:
        pass
    return data_dict
        
        
def create_DF_from_IMDb(m_data,vars_list):
    dicts=[]
    for d in m_data:
        #d=couple[1]
        movie={v:d.get(v,np.nan) for v in vars_list}
        #movie['Simple_Data']=title
        dicts.append(movie)
    DFrame=pd.DataFrame(dicts)
    DFrame['imdbID']=DFrame['imdbID'].apply(lambda s: 'tt'+s)
    return DFrame

def scrape_BOM_Year(year):
    link='https://www.boxofficemojo.com/year/{yr}/'.format_map({'yr':year})
    r=requests.get(link)
    soup=bs(r.content,'lxml')
    table=soup.find('div',attrs={'id':'table'})
    rows=table.findChildren('tr')
    #headers=list(rows[0].stripped_strings)
    movie_data={}
    for r in rows[1:]:
        l=r.a['href']
        movie_data[l]=list(r.stripped_strings)
    return movie_data


def scrape_BOM_title(imdb_id):
    imdb_id.replace('tt','')
    l='https://www.boxofficemojo.com/title/tt'+imdb_id
    d=dict.fromkeys(['domestic_gross','intl_gross',
                     'total_gross','imdb_id','budget']
                    )
    div_id2='mojo-summary-details-discloser'
    div_id1='a-section a-spacing-none mojo-performance-summary-table'
    r=requests.get(l)
    soup=bs(r.content,'lxml')
    t=soup.find('div',attrs={'class':div_id1})
    dom,intl,world=BOM_get_grosses(t)
    d['domestic_gross']=dom
    d['intl_gross']=intl
    d['total_gross']=world
    t=soup.find('div',attrs={'id':div_id2}).find_next('div')
    d['budget']=BOM_get_Budget(t)
    d['imdb_id']=imdb_id
    return(d)

def scrape_IMDb_from_BOM(ext):
    div_id='mojo-summary-details-discloser'

    l='https://www.boxofficemojo.com/'+ext
    r=requests.get(l)
    soup=bs(r.content,'lxml')
    t=soup.find('div',attrs={'id':div_id}).find_next('div')
    d=BOM_get_imdbID(t)
    return(d)

def scrape_from_BOM_release(ext):
    d={}
    div_id='mojo-summary-details-discloser'
    div_id1='a-section a-spacing-none mojo-performance-summary-table'
    l='https://www.boxofficemojo.com/'+ext
    r=requests.get(l)
    soup=bs(r.content,'lxml')
    t=soup.find('div',attrs={'class':div_id1})
    dom,intl,world=BOM_get_grosses(t)
    d['domestic_gross']=dom
    d['intl_gross']=intl
    d['total_gross']=world
    t=soup.find('div',attrs={'id':div_id}).find_next('div')
    d['budget']=BOM_get_Budget(t)
    d['imdbID']=BOM_get_imdbID(t)
    return(d)

def BOM_get_grosses(t):
    string=' '.join(t.stripped_strings)
    rgx_patt1=r'Domestic \( .{1,4}%{0,1} \) \$([0-9,]+)'
    rgx_patt2=r'International \( .{1,4}%{0,1} \) \$([0-9,]+)'
    rgx_patt3=r'Worldwide \$([0-9,]+)'
    d_search=regex.search(rgx_patt1,string)
    i_search=regex.search(rgx_patt2,string)
    w_search=regex.search(rgx_patt3,string)
    
    d=d_search.group(1) if d_search else '0'
    i=i_search.group(1) if i_search else '0'
    w=w_search.group(1) if w_search else '0'
    return d,i,w
def BOM_get_Budget(t):
    try:
        s=' '.join(t.stripped_strings)
        rgx_patt=r'Budget \$([0-9,]+)'
        x=regex.search(rgx_patt,s).group(1)
        return x
    except:
        return np.nan
def BOM_get_imdbID(t):
    s=t.find_all('a')[-1]['href']
    rgx_patt='https://pro.imdb.com/title/tt([0-9]+)'
    x=regex.search(rgx_patt,s).group(1)
    return x
