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
    author = item['author']
    author_stats = item['authorStats']
    new_row = {
        'uid': author['id'],
        'nickname': author['nickname'],
        'username': author['uniqueId'],
        'verified': author['verified'],
        'follower_count': author_stats['followerCount'],
        'like_count': author_stats['heartCount'],
        'video_count': author_stats['videoCount'],
        'hashtags': []
    }

    if 'textExtra' in item:
        for extra_items in item['textExtra']:
            new_row['hashtags'].append(extra_items['hashtagName'])
            print("adding a hashtag successfully", extra_items['hashtagName'])
        # Want to check if the author is already in the df
    if str(new_row['uid']) not in df.values:
        df = df.append(new_row, ignore_index=True)
        print("adding a new item")
    else:
        print("value found in dataframe")


df.to_csv("collected_data/authors.csv", index=False)
