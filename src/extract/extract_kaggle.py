import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
from utils import get_root_dir


def get_kaggle_data(root_dir:str, dataset_name: str, file_name: str):
    """Gets a dataset from kaggle and saves it to the storage/raw_data directory"""
    
    if not dataset_name:
        raise ValueError('Error: Provide name of Kaggle dataset.')

    if not file_name:
        raise ValueError('Error: Provide name of Kaggle file name.')

    df = kagglehub.load_dataset(KaggleDatasetAdapter.PANDAS, dataset_name, file_name)

    file_name = dataset_name.split('/')[1]

    # Save to storage as csv
    df.to_csv(f"{root_dir}\\storage\\raw\\{file_name}.csv", index=False)
