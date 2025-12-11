import os

import pytest
from dotenv import load_dotenv
from faker import Faker

load_dotenv()


@pytest.fixture
def faker() -> Faker:
    """
    The fixture provides client for Faker.
    The client has customizable locale.

    Returns:
        Faker: Faker object

    """

    locale: str = os.getenv("FAKER_LOCALE")

    return Faker(locale=locale)
