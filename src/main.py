from utils import get_root_dir, get_secret
from extract import extract_fred, extract_kaggle, extract_stripe
from load import load_duckdb

def run_pipeline():
    root_dir = get_root_dir.get_root()

    # extract Kaggle data
    # extract_kaggle.get_kaggle_data(root_dir, 'asinow/car-price-dataset/versions/1', 'car_price_dataset.csv')

    # extract FRED data
    fred_secret = get_secret.get_secret('fred_api_key')
    extract_fred.extract_fred_data(root_dir, fred_secret, 'cpi_gasoline', 'CUSR0000SETB01')

    # extract Stripe data
    stripe_secret = get_secret.get_secret('stripe_key')
    extract_stripe.get_data_from_stripe(stripe_secret, 'charge', 'https://api.stripe.com/v1/charges')

    # load data into duckdb
    load_duckdb(root_dir)

if __name__ == "__main__":
    run_pipeline()
