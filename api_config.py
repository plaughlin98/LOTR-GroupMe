import config
import requests


class LotrAPI:
    def __init__(self, URL, headers, end_point):
        self.URL = URL
        self.headers = headers
        self.end_point = end_point
        
    
    def get_data(self, end_point):
        request = requests.get(self.URL + '/' + self.end_point, headers=self.headers).json()
        response = request['docs']
        return response

