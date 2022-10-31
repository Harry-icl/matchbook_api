from http.client import HTTPException
import logging
import urllib.parse


DEFAULT_HEADERS = {
    "accept": "application/json",
    "User-Agent": "api-doc-test-client",
    "Accept-Encoding": "gzip"
}

def check_http_status_code(r):
    if r.status_code != 200:
        logging.error(f"HTTP error {r.status_code}: "
                      f"{r.json()['errors'][0]['messages']}")
        return HTTPException(f"HTTP error {r.status_code}: "
                             f"{r.json()['errors'][0]['messages']}")


def retrieve_data(r):
    if "Content-Encoding" in r.headers.keys() and r.headers["Content-Encoding"] == "gzip":
        pass


def add_kwargs_to_url(url, **kwargs):
    for k, v in kwargs.items():
        if isinstance(v, bool):
            v = str(v).lower()
        url += (urllib.parse.quote(k.replace('_', '-'))
                + "="
                + urllib.parse.quote(str(v))
                + "&")
    return url[:-1]


def create_kwarg_dict(**kwargs):
    kwarg_dict = {}
    for k, v in kwargs.items():
        if isinstance(v, bool):
            v = str(v).lower()
        kwarg_dict[k.replace('_', '-')] = v
    return kwarg_dict
