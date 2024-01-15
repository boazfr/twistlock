import pytest
import requests

from tests.utils.config import ENDPOINT
from tests.utils.credentials import AUTH
from tests.utils.utils import get_players_from_multiple_pages


@pytest.mark.headers
def test_response_headers():
    page_url = f"{ENDPOINT}?page=1"
    response = requests.get(page_url, auth=AUTH)
    assert 'Content-Type' in response.headers
    assert 'application/json' in response.headers[
        'Content-Type'], f"expected content type to be json but found {response.headers['Content-Type']}"


@pytest.mark.pagination
def test_large_page_number():
    page_url = f"{ENDPOINT}?page=10000"
    response = requests.get(page_url, auth=AUTH)
    status = response.status_code
    assert status == 200, f"expected status code 200 but got {status}"
    assert "error" not in response.json()


@pytest.mark.pagination
def test_negative_page():
    page_url = f"{ENDPOINT}?page=-1"
    response = requests.get(page_url, auth=AUTH)
    status = response.status_code
    assert status == 400, f"expected status code 400 but got {status}"


@pytest.mark.pagination
def test_non_numerical_page():
    page_url = f"{ENDPOINT}?page=x"
    response = requests.get(page_url, auth=AUTH)
    status = response.status_code
    assert status == 400, f"expected status code 400 but got {status}"


@pytest.mark.data
def test_data_properties():
    first_page = f"{ENDPOINT}?page=1"
    response = requests.get(first_page, auth=AUTH)
    players = response.json()
    for player in players:
        assert "Name" in player, "player is missing a Name property!"
        assert "ID" in player, "player is missing an ID property!"


@pytest.mark.data
def test_players_names():
    first_page = f"{ENDPOINT}?page=1"
    response = requests.get(first_page, auth=AUTH)
    players = response.json()
    for player in players:
        assert len(player['Name']) > 0, f"player {player['ID']} has no name!"


@pytest.mark.data
def test_players_ids():
    first_page = f"{ENDPOINT}?page=1"
    response = requests.get(first_page, auth=AUTH)
    players = response.json()
    for player in players:
        assert len(str(player['ID'])) > 0, f"player {player['Name']} has no id!"


@pytest.mark.data
def test_consecutive_players_in_page():
    players = get_players_from_multiple_pages(1, 1)
    for i in range(1, len(players)):
        current_id = players[i]['ID']
        previous_id = players[i - 1]['ID']
        assert current_id == previous_id + 1, f"found non consecutive players! {players[i]} and {players[i - 1]}"


@pytest.mark.data
def test_consecutive_players_in_multiple_pages():
    # let's say there are 10 pages of players
    for i in range(2, 11):
        players_current_page = get_players_from_multiple_pages(i, i)
        players_previous_page = get_players_from_multiple_pages(i - 1, i - 1)

        assert players_current_page[0]['ID'] == players_previous_page[-1]['ID'] + 1, (f"found non matching consecutive "
                                                                                      f"ID's!")
