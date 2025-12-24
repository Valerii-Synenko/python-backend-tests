import os

import pytest
from dotenv import load_dotenv
from faker import Faker

from src.api_clients.user_client import UserClient

load_dotenv()


@pytest.fixture
def faker() -> Faker:
    """
    The fixture provides client for Faker.
    The client has customizable locale. If the FAKER_LOCALE is unset, the `en_US` will be used as a default.

    Returns:
        Faker: Faker object with specified locale.

    """
    locale: str | None = os.getenv("FAKER_LOCALE", "en_US")
    return Faker(locale=locale)


@pytest.fixture
def user_client():
    """Crete UserClient object. And after test close the session."""
    client = UserClient()
    yield client
    client.close_session()
