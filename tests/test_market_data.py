from matchbook_api import Client


client = Client()
client.login()


def test_get_sports():
    sports = client.get_sports()
    assert 'sports' in sports.keys()
    assert len(sports['sports']) > 0


def test_get_navigation():
    navigation = client.get_navigation()
    assert isinstance(navigation, list)
    assert len(navigation) > 0


def test_get_events():
    events = client.get_events()
    assert 'events' in events.keys()
    assert len(events['events']) > 0


events = client.get_events()
event_id = events['events'][0]['id']


def test_get_event():
    event = client.get_event(event_id)
    assert isinstance(event, dict)


def test_get_markets():
    markets = client.get_markets(event_id)
    assert 'markets' in markets.keys()
    assert isinstance(markets['markets'], list)


markets = client.get_markets(event_id)



def test_get_market():
    pass
