from http.client import HTTPException


DEFAULT_HEADERS = {
    "accept": "application/json",
    "User-Agent": "api-doc-test-client"
}

def check_http_status_code(r):
    if r.status_code != 200:
        raise HTTPException(f"HTTP error {r.status_code}: {r.json()['errors']['messages']}")
