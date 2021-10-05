import config
import requests
import pandas as pd

headers = {
    'X-API-KEY': config.api_key
}

# create a dataframe to store the following information
columns = ['user', 'follower_count', 'category']

df = pd.DataFrame(columns=columns)

# makes a request to query the max number of videos from popular feed
r = requests.get(url='https://api.tikapi.io/public/explore?count=30',
                 headers=headers)


df.to_csv()
