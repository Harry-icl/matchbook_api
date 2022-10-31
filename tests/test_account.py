from matchbook_api import Client


def test_get_account():
    client = Client()
    client.login()
    account = client.get_account()
    key_list = [
        'id', 'username', 'status', 'commission-type', 'currency', 'country',
        'balance', 'exposure', 'commission-reserve', 'free-funds', 'language',
        'language', 'exchange-type', 'odds-type', 'show-bet-confirmation',
        'show-position', 'show-odds-rounding-message', 'bet-slip-pinned',
        'roles'
    ]
    for key in key_list:
        assert key in account.keys()


def test_get_balance():
    client = Client()
    client.login()
    balance = client.get_balance()
    key_list = [
        'id', 'balance', 'exposure', 'commission-reserve', 'free-funds'
    ]
    for key in key_list:
        assert key in balance.keys()
