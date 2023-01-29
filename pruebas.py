from api.request_api import Request

instance = Request('https://pokeapi.co/api/v2/pokemon')
api = instance.get_api()
#print(f"Pokemon: {api['results'][5]['name']}, Link: {api['results'][5]['url']}")
print(api)