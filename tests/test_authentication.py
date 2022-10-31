from matchbook_api import Client


def test_login():
    client = Client(log=False)
    assert not isinstance(client.login(), Exception)


def test_logout():
    client = Client(log=False)
    client.login()
    assert not isinstance(client.logout(), Exception)


def test_validate_session():
    client = Client(log=False)
    assert not isinstance(client.login(), Exception)
    assert client.validate_session()
