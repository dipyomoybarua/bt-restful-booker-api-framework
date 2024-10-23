import requests
from .auth_provider import AuthProvider

class BaseAPI:
    def __init__(self):
        self.base_url = "https://restful-booker.herokuapp.com"
        self.auth_provider = AuthProvider()
        self.token = self._get_token()

    def _get_token(self):
        auth_data = self.auth_provider.get_auth_data()
        response = requests.post(f"{self.base_url}/auth", json=auth_data)
        if response.status_code == 200:
            return response.json()['token']
        else:
            raise Exception("Failed to authenticate")

    def get_headers(self, is_json=True):
        headers = {
            "Cookie": f"token={self.token}"
        }
        if is_json:
            headers["Content-Type"] = "application/json"
            headers["Accept"] = "application/json"
        return headers
