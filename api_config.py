import config
import requests


class LotrAPI:
    def __init__(self, URL, headers):
        self.URL = URL
        self.headers = headers
        
    
    def get_data(self, end_point):
        request = requests.get(self.URL + '/' + end_point, headers=self.headers).json()
        response = request['docs']
        return response

