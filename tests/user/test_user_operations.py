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
import json

import requests

from src.models.requests.register_user_requests import RegisterUserModel


class TestUserOperations:

    def test_user_registration(self):

        user = {
            "username": "testuser123",
            "password": "password123",
            "email": "test123@example.com",
            "firstName": "John",
            "lastName": "Doe",
        }

        in_pay = RegisterUserModel(
            username="SuperUser",
            password="password123-2",
            email="test123-2@email.com",
        )

        url = "http://localhost/register"


        response = requests.post(
            url=url,
            headers={"Content-Type": "application/json"},
            data=in_pay.model_dump()
        )

        assert response.status_code == 200
