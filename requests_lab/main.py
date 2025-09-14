from config.definitions import NASA_BASE_URL, NASA_DEMO_KEY, POKE_BASE_URL, JSONPL_BASE_URL
from service.get import get_url_data
from service.post import post_to_jsonplaceholder


### NASA CALL 
params = {"api_key": NASA_DEMO_KEY}
data = get_url_data(NASA_BASE_URL, params)
print(data.keys())

## POKE CALL
params = {"limit": 3, "offset": 0}
data = get_url_data(POKE_BASE_URL, params)

[print(f"name: {pokemon['name']}") for pokemon in data["results"]]

## POST TO VOID URL
data = {
  "title": "test title",
  "body": "test body",
  "userId": 1
}
data = post_to_jsonplaceholder(f"{JSONPL_BASE_URL}/posts", data)

print(data)