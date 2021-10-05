import config
import requests
import pandas as pd

headers = {
    'X-API-KEY': config.api_key
}

# create a dataframe to store the following information
columns = ['uid', 'nickname', 'username', 'verified', 'follower_count',
           'like_count', 'video_count', 'hashtags']

df = pd.read_csv("collected_data/authors.csv")
print("using old df found in hard-drive")
if len(df.index) == 0:
    df = pd.DataFrame(columns=columns)
    print("using new df")

# makes a request to query the max number of videos from popular feed
r = requests.get(url='https://api.tikapi.io/public/explore?count=30',
                 headers=headers)

response = r.json()
print(r.status_code)

for item in response['itemList']:
    print("adding a new item")
    author = item['author']
    author_stats = item['authorStats']

    new_row = {
        'uid': author['id'],
        'nickname': author['nickname'],
        'username': author['uniqueId'],
        'verified': author['verified'],
        'follower_count': author_stats['followerCount'],
        'like_count': author_stats['heartCount'],
        'video_count': author_stats['videoCount']
    }
    print(new_row)

    df = df.append(new_row, ignore_index=True)


df.to_csv("collected_data/authors.csv")
