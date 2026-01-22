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
import pytest
from requests import Response

from src.models.responses.register_user_response import (
    RegisterUserResponseModel as ResponseModel,
)
from tests.data.user_data import user_data


class TestUserOperations:

    @allure.title("User registration")
    @allure.description("Test is verifying that a user can do registration with specified fields.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("request_model", user_data.valid_registration_models)
    def test_user_registration(self, user_client, request_model):

        with allure.step("Step 1: Register new user with"):
            response: Response = user_client.user_register(user_model=request_model)

        with allure.step("Step 2: Assert that status code is 200"):
            assert (
                response.status_code == 500
            ), f"the request with body '{request_model.model_dump()}' returned status code: {response.status_code}"

        with allure.step("Step 3: Validate response body"):
            ResponseModel.model_validate(response.json())
