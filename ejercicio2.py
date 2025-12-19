import requests
r = requests.get("https://pokeapi.co/api/v2/pokemon", params={"limit": 10})
data = r.json()
for p in data["results"]:
    print(p["name"])