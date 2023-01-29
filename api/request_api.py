import requests
import json

class Request:
    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    def get_api(self):
        request_data = requests.get(self.url)
        convert_to_json = request_data.json()
        return convert_to_json

    def __str__(self):
        string = f'The API´s link is: {self.url}'
        return string



    
    
