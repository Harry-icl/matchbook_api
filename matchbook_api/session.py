import requests
from http.client import HTTPException

from .utils import DEFAULT_HEADERS, check_http_status_code


class Session:
    def __init__(self):
        self.url = "https://api.matchbook.com/"
        self.session = requests.Session()
        self.session_token = None

    def post(self, url, payload_data, headers=DEFAULT_HEADERS):
        r = self.session.post(url, data=payload_data, headers=headers)
        check_http_status_code(r)
        data = r.json()
        return data

    def delete(self, url, headers=DEFAULT_HEADERS):
        r = self.session.delete(url, headers=headers)
        check_http_status_code(r)
        data = r.json()
        return data

    def get(self, url, headers=DEFAULT_HEADERS):
        r = self.session.get(url, headers=headers)
        check_http_status_code(r)
        data = r.json()
        return data

    def put(self, url, json, headers=DEFAULT_HEADERS):
        r = self.session.put(url, json=json, headers=headers)
        check_http_status_code(r)
        data = r.json()
        return data
