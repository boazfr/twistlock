import time
from concurrent.futures import ThreadPoolExecutor

import pytest
import requests

from tests.utils.config import ENDPOINT
from tests.utils.credentials import AUTH
from tests.utils.utils import get_players_on_page


@pytest.mark.performance
def test_concurrent_requests():
    # An arbitrary number of concurrent requests to test if the API crashes
    # If you change the number to 10, for example, the test will fail and the web server will crash
    num_requests = 3

    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(get_players_on_page, page_number) for page_number in range(1, num_requests + 1)]

        for i, future in enumerate(futures, start=1):
            try:
                result = future.result()
                status = result.status_code
                assert status == 200, f"expected status 200 but got {status} for request {i}"
            except Exception as e:
                print(f"Error in Request {i}: {e}")
                status = result.status_code
                assert "Error" not in status, f"found status {status}"


@pytest.mark.performance
def test_response_time():
    page_url = f"{ENDPOINT}?page=1"
    start_time = time.time()
    response = requests.get(page_url, auth=AUTH)
    end_time = time.time()
    response_time = end_time - start_time
    print(response_time)
    # I chose 0.1 seconds as an arbitrary benchmark
    assert response_time < 0.1, f"expected response time to be less than 0.1 second but it was {response_time}"
    status = response.status_code
    assert status == 200, f"expected status code 200 but got {status}"
