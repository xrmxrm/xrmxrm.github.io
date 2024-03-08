import requests

headers = {'User-Agent': '<my-url>', 'Accept':"application/json"}

query_params = {'page':1, 'limit':4, 'term':"bike"}
r = requests.get('https://icanhazdadjoke.com/search', headers=headers,  params=query_params)

print(r.status_code)
print(r.json())