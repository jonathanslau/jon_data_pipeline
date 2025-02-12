import requests
import pandas as pd

def extract_fred_data(root_dir:str, API_KEY: str, data_series_name:str, data_series_id: str):
    """Retrieve economic series from St Louis FED"""

    if not data_series_id:
        raise ValueError('Error: Provide FRED series ID.')

    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={data_series_id}&api_key={API_KEY}&file_type=json"

    response = requests.get(url)

    data = response.json()['observations']
    data = pd.DataFrame(data)
    data['value'] = data['value'].replace('.', 0.0)
    # data['value'] = data['value'].astype(float)

    # Save to storage as csv
    data.to_csv(f"{root_dir}\\storage\\raw\\{data_series_name}.csv", index=False)
