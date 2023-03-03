import requests
import json

# This script works with PokeAPI, All the Pokémon data you'll ever need in one place: https://pokeapi.co/
# This class handles the API connection and data request.

class Request:
    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    def get_api(self): # Gets the  data of the API and transform the request to JSON, then, returns it.
        request_data = requests.get(self.url)
        convert_to_json = request_data.json()
        return convert_to_json

    def __str__(self):
        string = f'The API´s link is: {self.url}'
        return string




    
    
