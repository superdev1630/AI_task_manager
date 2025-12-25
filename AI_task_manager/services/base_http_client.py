import requests
from typing import Dict


class BaseHTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-type": "application/json",
            "Accept": "application/json"
        }

    def postCall(self, endpoint: str, data):
        print("URL", f"{self.base_url}/{endpoint}")
        print("POSTBODY", data)
        response = requests.post(
            f"{self.base_url}/{endpoint}", headers=self.headers, json=data)
        return response.json()

    def getCall(self, endpoint: str):
        response = requests.get(
            f"{self.base_url}/{endpoint}", headers=self.headers)
        return response.json()

    def putCall(self, endpoint: str, data):
        print("PUTBODY", data)
        response = requests.put(
            f"{self.base_url}/{endpoint}", headers=self.headers, json=data)
        return response.json()
