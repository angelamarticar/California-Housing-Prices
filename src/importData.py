from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    """
        Imports the housing dataset from GitHub
    """
    dataset_path= Path("data/housing.tgz") 
    if not dataset_path.is_file(): 
        Path("data").mkdir(parents=True, exist_ok=True) 
        url= "https://github.com/ageron/data/raw/main/housing.tgz"  
        urllib.request.urlretrieve(url, dataset_path)
    with tarfile.open(dataset_path) as housing_file:
        housing_file.extractall(path="data")
    return pd.read_csv(Path("data/housing/housing.csv"))

housing = load_housing_data()