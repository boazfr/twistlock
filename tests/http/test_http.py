import pytest
import requests

from tests.utils.config import ENDPOINT
from tests.utils.credentials import AUTH


@pytest.mark.http
def test_add_player_post():
    response = requests.post(ENDPOINT, auth=AUTH, data={'Name': 'blabla', 'ID': '-1'})
    status = response.status_code
    assert status == 403, f"expected status code 403 but got {status}"


@pytest.mark.http
def test_add_player_put():
    response = requests.put(ENDPOINT, auth=AUTH, data={'Name': 'blabla', 'ID': '10'})
    status = response.status_code
    assert status == 403, f"expected status code 403 but got {status}"


@pytest.mark.http
def test_add_player_patch():
    response = requests.patch(ENDPOINT, auth=AUTH, data={'Name': 'blabla', 'ID': '10'})
    status = response.status_code
    assert status == 403, f"expected status code 403 but got {status}"


@pytest.mark.http
def test_delete_players():
    page_url = f"{ENDPOINT}?page=1"
    response = requests.delete(page_url, auth=AUTH)
    status = response.status_code
    assert status == 403, f"expected status code 403 but got {status}"
