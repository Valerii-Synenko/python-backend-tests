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

import allure

from src.models.requests.register_user_requests import RegisterUserRequestsModel
from src.models.responses.register_user_response import RegisterUserResponseModel


class TestUserOperations:

    def test_user_registration_with_valid_creds(self, user_client, faker):

        with allure.step("Step 1: Register new user"):
            user_model = RegisterUserRequestsModel(
                username=faker.user_name(),
                email=faker.email(),
                password=faker.password(),
            )

            response = user_client.user_register(user_model=user_model)

        with allure.step("Step 2: Assert that status code is 200"):
            assert (
                response.status_code == 200
            ), f"the request with {user_model.model_dump()} returned status code: {response.status_code}"

        with allure.step("Step 3: Validate response body"):
            RegisterUserResponseModel.model_validate(response.json())
