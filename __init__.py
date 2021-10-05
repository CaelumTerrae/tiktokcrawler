import requests

headers = {
    'X-API-KEY': 'test key goes here'
}

r = requests.get(url='https://api.tikapi.io/public/explore?count=5',
                 headers=headers)

print(r.json())
