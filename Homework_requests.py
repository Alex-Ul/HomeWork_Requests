import requests
from pprint import pprint

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)

heros_list = ['Hulk', 'Captain America', 'Thanos']
heros_intel = {}

for profile in response.json():
    if profile['name'] in heros_list:
        heros_intel[profile['name']] = profile['powerstats']['intelligence']

print(f"Самый умный супергерой {max(heros_intel)}. Его уровень интеллекта {max(heros_intel.values())}")
