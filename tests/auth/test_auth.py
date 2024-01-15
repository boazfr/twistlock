import pytest
import requests

from tests.utils.config import ENDPOINT
from tests.utils.credentials import AUTH, INVALID_USER_AUTH, INVALID_PASSWORD_AUTH


@pytest.mark.auth
def test_auth_valid_with_page():
    page_url = f"{ENDPOINT}?page=1"
    response = requests.get(page_url, auth=AUTH)
    status = response.status_code
    assert status == 200, f"expected status code 200 but got {status}"


@pytest.mark.auth
def test_auth_valid_without_page():
    response = requests.get(ENDPOINT, auth=AUTH)
    status = response.status_code
    assert status == 403, f"expected status code 200 but got {status}"


@pytest.mark.auth
def test_auth_without_credentials():
    response = requests.get(ENDPOINT)
    status = response.status_code
    assert status == 401, f"expected status code 401 but got {status}"


@pytest.mark.auth
def test_auth_invalid_user():
    page_url = f"{ENDPOINT}?page=1"
    response = requests.get(page_url, auth=INVALID_USER_AUTH)
    status = response.status_code
    assert status == 401, f"expected status code 401 but got {status}"


@pytest.mark.auth
def test_auth_invalid_password():
    page_url = f"{ENDPOINT}?page=1"
    response = requests.get(page_url, auth=INVALID_PASSWORD_AUTH)
    status = response.status_code
    assert status == 401, f"expected status code 401 but got {status}"
