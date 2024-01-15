import requests

from tests.utils.credentials import AUTH
from tests.utils.config import ENDPOINT


def get_players_on_page(page_number):
    page_url = f"{ENDPOINT}?page={page_number}"
    response = requests.get(page_url, auth=AUTH)

    if response.status_code == 200:
        return response
    else:
        response.raise_for_status()


def get_players_from_multiple_pages(start, end):
    players = []
    for page in range(start, end + 1):
        page = f"{ENDPOINT}?page={page}"
        response = requests.get(page, auth=AUTH)
        players_on_page = response.json()
        players.extend(players_on_page)

    print(players)
    return players
