from glob import glob
import pandas as pd

def get_file_paths():
    return glob('./raw_data/*')

def save_locs(data, path, type):
    if type == 'csv':
        data.to_csv('.'.join((path, type)))
    elif type == 'json':
        data.to_json('.'.join((path, type)), orient="records")