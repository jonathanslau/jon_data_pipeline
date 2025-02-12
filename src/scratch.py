from utils import get_root_dir, get_secret
from extract import extract_kaggle, extract_fred_data
from load import load_duckdb

if __name__ == "__main__":
    root_dir = get_root_dir.get_root()
    load_duckdb.load_data_to_duckdb(root_dir)
