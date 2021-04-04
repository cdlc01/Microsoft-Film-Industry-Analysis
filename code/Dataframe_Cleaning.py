## DATAFRAME CLEANING FUNCTION

import pandas as pd

def imdb_clean():

    dirty_data = pd.read_pickle("data/Final_UnFromatted_wGross.pkl")

    len_list = []
    month_list = []

    for i in range(2563):
        if type(dirty_data['plot outline'][i]) == float:
            len_list.append(None)
        else:
            len_list.append(len(dirty_data['plot outline'][i]))

    for i in range(2563):
        if type(dirty_data['original air date'][i]) == float:
            month_list.append(None)
        else:
            month_list.append(dirty_data['original air date'][i][3:6])

    dirty_data['synopsis_len'] = len_list
    dirty_data['month'] = month_list

    cleaned_data = dirty_data.drop(columns = ['runtimes', 'cast', 'country codes', 'director', 'language codes', 'production companies', 'certificates', 'box office'])
      
    return cleaned_data
