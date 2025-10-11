import pandas as pd
import numpy as np


def get_all_data(paths):
    all_data = pd.DataFrame()

    for path in paths:
        # Get the year from path
        year = path.split("-")[1][:4]
        data = pd.read_csv(path, sep=",")
        # We do not want certain columns, so drop
        
        
        # If we wanted to add the year to the data
        #year_vector = int(year) * np.ones(data.shape[0])
        #data.insert(len(data.columns), 'year', year_vector)
        
        all_data = pd.concat([all_data, data])
    return all_data


def get_year_data(year):
    path = f'./raw_data/{year-1}-{year}comp.csv'
    return pd.read_csv(path, sep=","), year