"""
User operations API tests.

This module contains tests for user actions API endpoints including
registration, authentication, and customer operation.

Endpoints:
    /register (POST)
    /login (GET)
    /customers (GET, DELETE)

Typical usage example:
    pytest tests/test_user_operations.py
    pytest tests/test_user_operations.py::TestUserOperations::test_user_registration
"""

import os

import requests
from dotenv import load_dotenv

from src.models.requests.register_user_requests import RegisterUserRequestsModel
from src.models.responses.register_user_response import RegisterUserResponseModel

load_dotenv()


class TestUserOperations:

    def test_user_registration_with_valid_creds(self, faker):

        user_model = RegisterUserRequestsModel(
            username=faker.user_name(),
            email=faker.email(),
            password=faker.password(),
        )

        response = requests.post(
            url=f"{os.getenv('BASE_URL')}/register",
            headers={"Content-Type": "application/json"},
            data=user_model.model_dump_json(),
        )

        assert response.status_code == 200

        RegisterUserResponseModel.model_validate(response.json())
