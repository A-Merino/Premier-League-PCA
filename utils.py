from glob import glob
import pandas as pd

def get_file_paths():
    return glob('./raw_data/*')

def save_locs(data, path):
    data.to_csv(path)