import requests
from requests.auth import HTTPBasicAuth
import pandas as pd


def get_data_from_stripe(key: str, stripe_object_name: str, url: str):

    # empty list to append api response data to
    data = []

    # pagination
    params = {
        'limit': 100
    }
    has_more = True

    # pagination loop
    while has_more:
        
        # stripe uses basic auth over https
        response = requests.get(url, auth=HTTPBasicAuth(key, ''), params=params)
        response_data = response.json().get('data', [])

        # append to main list
        data.extend(response_data)

        # check for next page
        has_more = response.json().get('has_more', False)

        # stripe's method of pagination is based on querying on reverse-chronological order of record ids
        if has_more:
            params['starting_after'] = response_data[-1]["id"]

    # finish up
    # convert list of jsons to dataframe, save dataframe to storage
    
    df = pd.json_normalize(data, max_level=0)
    df.to_csv(f"C:\\Users\\auslj\\jon_data_pipeline\\storage\\raw\\{stripe_object_name}.csv", index=False)
