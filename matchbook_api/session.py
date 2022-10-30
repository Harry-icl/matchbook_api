import requests
import logging

from .utils import DEFAULT_HEADERS, check_http_status_code


class Session:
    def __init__(self, log: bool = True):
        self.url = "https://api.matchbook.com/"
        self.session = requests.Session()
        self.session_token = None
        if log:
            self.session_logging_file = "session.log"
            logging.basicConfig(filename=self.session_logging_file, encoding='utf-8', level=logging.INFO)

    def post(self, url, json, headers=DEFAULT_HEADERS):
        r = self.session.post(self.url + url, json=json, headers=headers)
        error = check_http_status_code(r)
        if isinstance(error, Exception):
            return error
        else:
            logging.info("HTTP POST request returned 200 (success).")
            data = r.json()
            return data

    def delete(self, url, headers=DEFAULT_HEADERS):
        r = self.session.delete(self.url + url, headers=headers)
        error = check_http_status_code(r)
        if isinstance(error, Exception):
            return error
        else:
            logging.info("HTTP DELETE request returned 200 (success).")
            data = r.json()
            return data

    def get(self, url, headers=DEFAULT_HEADERS):
        r = self.session.get(self.url + url, headers=headers)
        error = check_http_status_code(r)
        if isinstance(error, Exception):
            return error
        else:
            logging.info("HTTP GET request returned 200 (success).")
            data = r.json()
            return data

    def put(self, url, json, headers=DEFAULT_HEADERS):
        r = self.session.put(self.url + url, json=json, headers=headers)
        error = check_http_status_code(r)
        if isinstance(error, Exception):
            return error
        else:
            logging.info("HTTP PUT request returned 200 (success).")
            data = r.json()
            return data
