import json
import logging
from numpy import datetime64

from .session import Session
from .utils import add_kwargs_to_url


class Client:
    def __init__(self, username, password, log: bool = True):
        self.username = username
        self.password = password
        self.session = Session(log)
        self.session_token = None
        if log:
            self.client_logging_file = "client.log"
            logging.basicConfig(filename=self.client_logging_file, encoding='utf-8', level=logging.INFO)
    
    def login(self):
        url = "bpapi/rest/security/session"
        payload = {
            "username": self.username,
            "password": self.password
        }
        headers = {
            "content-type": "application/json;charset=UTF-8",
            "accept": "*/*"
        }

        data = self.session.post(url, json.dumps(payload), headers)
        if isinstance(data, Exception):
            logging.error("Login failed.")
            return data
        else:
            self.session_token = data['session-token']
            self.user_id = data['user-id']
            logging.info("Login successful.")

    def logout(self):
        url = "bpapi/rest/security/session"
        
        data = self.session.delete(url)
        if isinstance(data, Exception):
            logging.error("Logout failed.")
            return data
        else:
            self.session_token = None
            logging.info("Logout successful.")
    
    def validate_session(self):
        url = "bpapi/rest/security/session"
        data = self.session.get(url)
        if isinstance(data, Exception):
            logging.info("Session check: not active.")
            return False
        else:
            logging.info("Session check: active.")

    def get_account(self):
        url = "edge/rest/account"

        data = self.session.get(url)
        return data

    def get_balance(self):
        url = "edge/rest/account/balance"
        
        data = self.session.get(url)
        return data

    def get_sports(self, offset: int = 0, per_page: int = 20, order: str = "name asc"):
        url = "edge/rest/lookups/sports?"
        params = locals()
        del params['self']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    def get_navigation(self, offset: int = 0, per_page: int = 20):
        url = "edge/rest/navigation?"
        params = locals()
        del params['self']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    def get_events(self, offset: int = 0, per_page: int = 20,
                   states: str = "open,suspended,closed,graded",
                   exchange_type: str = "back-lay", odds_type: str = "DECIMAL",
                   include_prices: bool = False, price_depth: int = 3,
                   price_mode: str = "expanded",
                   include_event_participants: bool = False,
                   exclude_mirrored_prices: bool = False, **kwargs):
        url = "edge/rest/events?"
        params = locals()
        del params['self']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    def get_event(self, event_id: int, exchange_type: str = "back-lay",
                  odds_type: str = "DECIMAL", include_prices: bool = False,
                  price_depth: int = 3, price_mode: str = "expanded",
                  include_event_participants: bool = False,
                  exclude_mirrored_prices: bool = False, **kwargs):
        url = f"edge/rest/events/{event_id}?"
        params = locals()
        del params['self']
        del params['event_id']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    def get_markets(self, event_id: int, offset: int = 0, per_page: int = 20,
                    states: str = "open,suspended",
                    exchange_type: str = "back-lay",
                    odds_type: str = "DECIMAL", include_prices: bool = False,
                    price_depth: int = 3, price_mode: str = "expanded",
                    exclude_mirrored_prices: bool = False, **kwargs):
        url = f"edge/rest/events/{event_id}?"
        params = locals()
        del params['self']
        del params['event_id']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data
    
    def get_market(self, event_id: int, market_id: int,
                   exchange_type: str = "back-lay", odds_type: str = "DECIMAL",
                   include_prices: bool = False, price_depth: int = 3,
                   price_mode: str = "expanded",
                   exclude_mirrored_prices: bool = False, **kwargs):
        url = f"edge/rest/events/{event_id}/markets/{market_id}?"
        params = locals()
        del params['self']
        del params['event_id']
        del params['market_id']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    
