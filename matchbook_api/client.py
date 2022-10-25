import json
from http.client import HTTPException

from .session import Session
from .enums import Order


class Client:
    def __init__(self, username, password, locale):
        self.username = username
        self.password = password
        self.locale = locale
        self.session = Session()
        self.session_token = None
    
    def login(self):
        url = self.url + "bpapi/rest/security/session"
        payload = {
            "username": self.username,
            "password": self.password
        }
        headers = {
            "content-type": "application/json;charset=UTF-8",
            "accept": "*/*"
        }

        data = self.session.post(url, json.dumps(payload), headers)
        self.session_token = data['session-token']

    def logout(self):
        url = self.url + "bpapi/rest/security/session"
        
        data = self.session.delete(url)
        self.session_token = None
    
    def validate_session(self):
        url = self.url + "bpapi/rest/security/session"

        try:
            data = self.session.get(url)
            return True
        except(HTTPException):
            return False

    def get_account(self):
        url = self.url + "edge/rest/account"

        data = self.session.get(url)
        return data

    def get_balance(self):
        url = self.url + "edge/rest/account/balance"
        
        data = self.session.get(url)
        return data

    def get_sports(self, offset: int = 0, per_page: int = 20, order: Order = Order.NAME_ASC):
        url = self.url + f"edge/rest/lookups/sports?offset={offset}&per-page={per_page}&order={order.value}&status=active"

        data = self.session.get(url)
        return data

    def get_navigation(self, offset: int = 0, per_page: int = 20):
        url = self.url + f"edge/rest/navigation?offset={offset}&per-page={per_page}"

    def get_events(self):
        pass

    def get_event(self):
        pass
    