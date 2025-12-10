import pytest

BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL
