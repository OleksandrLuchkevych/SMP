import requests

class APIRepository:

    BASE_URL = 'https://jsonplaceholder.typicode.com'

    def __init__(self):
        self.session = requests.Session()

    def get_posts(self):
        response = self.session.get(f'{self.BASE_URL}/posts')
        response.raise_for_status()
        return response.json()

    def get_users(self):
        response = self.session.get(f'{self.BASE_URL}/users')
        response.raise_for_status()
        return response.json()