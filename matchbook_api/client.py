import logging
from numpy import datetime64
from typing import List

from .session import Session
from .utils import add_kwargs_to_url, create_kwarg_dict


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

        data = self.session.post(url, payload, headers)
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
        url = f"edge/rest/events/{event_id}/markets?"
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

    def get_runners(self, event_id: int, market_id: int,
                    states: str = "open,suspended",
                    include_withdrawn: bool = True,
                    include_prices: bool = True, price_depth: int = 3,
                    price_mode: str = "expanded",
                    exchange_type: str = "back-lay",
                    odds_type: str = "DECIMAL",
                    exclude_mirrored_prices: bool = False, **kwargs):
        url = f"edge/rest/events/{event_id}/markets/{market_id}/runners?"
        params = locals()
        del params['self']
        del params['event_id']
        del params['market_id']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    def get_runner(self, event_id: int, market_id: int, runner_id: int,
                   include_prices: bool = False, price_depth: int = 3,
                   price_mode: str = "expanded",
                   exchange_type: str = "back-lay", odds_type: str = "DECIMAL",
                   exclude_mirrored_prices: bool = False, **kwargs):
        url = (f"edge/rest/events/{event_id}/markets/{market_id}/runners/"
               f"{runner_id}?")
        params = locals()
        del params['self']
        del params['event_id']
        del params['market_id']
        del params['runner_id']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    def get_prices(self, event_id: int, market_id: int, runner_id: int,
                   exchange_type: str = "back-lay", odds_type: str = "DECIMAL",
                   depth: int = 3, price_mode: str = "expanded",
                   exclude_mirrored_prices: bool = False, **kwargs):
        url = (f"edge/rest/events/{event_id}/markets/{market_id}/runners/"
               f"{runner_id}/prices?")
        params = locals()
        del params['self']
        del params['event_id']
        del params['market_id']
        del params['runner_id']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data
    
    def get_popular_markets(self, exchange_type: str = "back-lay",
                            odds_type: str = "DECIMAL", price_depth: int = 3,
                            price_mode: str = "expanded",
                            old_format: bool = False, **kwargs):
        url = "edge/rest/popular-markets?"
        params = locals()
        del params['self']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data
    
    def get_popular_sports(self, num_sports: int = 5):
        url = "edge/rest/popular/sports?"
        params = locals()
        del params['self']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    def submit_offers(self, offers: List[dict], odds_type: str = "DECIMAL",
                      exchange_type: str = "back-lay"):
        url = "edge/rest/v2/offers"
        payload = {
            "exchange-type": exchange_type,
            "odds-type": odds_type,
            "offers": {"offers": offers}
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "api-doc-test-client",
            "content-type": "application/json",
            "Accept-Encoding": "gzip"
        }

        data = self.session.post(url, payload, headers)
        return data

    def edit_offers(self, offers: List[dict]):
        url = "edge/rest/v2/offers"
        payload = {
            {"offers": {"offers": offers}}
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "api-doc-test-client",
            "content-type": "application/json",
            "Accept-Encoding": "gzip"
        }

        data = self.session.put(url, payload, headers)
        return data

    def edit_offer(self, offer_id: int, **kwargs):
        url = f"edge/rest/v2/offers/{offer_id}"
        payload = create_kwarg_dict(**kwargs)
        headers = {
            "accept": "application/json",
            "User-Agent": "api-doc-test-client",
            "content-type": "application/json",
            "Accept-Encoding": "gzip"
        }

        data = self.session.put(url, payload, headers)
        return data

    def cancel_offers(self, **kwargs):
        url = "edge/rest/v2/offers"
        url = add_kwargs_to_url(url, **kwargs)

        data = self.session.delete(url)
        return data
    
    def cancel_offer(self, offer_id: int):
        url = f"edge/rest/v2/offers/{offer_id}"

        data = self.session.delete(url)
        return data
    
    def get_offers(self, offset: int = 0, per_page: int = 20,
                   include_edits: bool = False, **kwargs):
        url = "edge/rest/v2/offers?"
        params = locals()
        del params['self']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    def get_offer(self, offer_id: int, include_edits: bool = False):
        url = (f"edge/rest/v2/offers/{offer_id}?include-edits="
               f"{str(include_edits).lower()}")
        
        data = self.session.get(url)
    
    def get_aggregated_matched_bets(self, offset: int = 0, per_page: int = 20,
                                    aggregation_type: str = "average",
                                    **kwargs):
        url = "edge/rest/bets/matched/aggregated?"
        params = locals()
        del params['self']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    def get_cancelled_matched_bets(self):
        url = "bets?status=cancelled"

        data = self.session.get(url)
        return data

    def get_positions(self, offset: int = 0, per_page: int = 20, **kwargs):
        url = "edge/rest/account/positions?"
        params = locals()
        del params['self']
        url = add_kwargs_to_url(url, **params)

        data = self.session.get(url)
        return data

    def get_offer_edits(self, offer_id: int, offset: int = 0,
                        per_page: int = 20):
        url = (f"edge/rest/v2/offers/{offer_id}/offer-edits?offset={offset}&pe"
               f"r-page={per_page}")

        data = self.session.get(url)
        return data

    def get_offer_edit(self, offer_id: int, offer_edit_id: int):
        url = f"edge/rest/v2/offers/{offer_id}/offer-edits/{offer_edit_id}"

        data = self.session.get(url)
        return data

    
