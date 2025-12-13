"""
Base client for API interactions.

This module provides the base client class that should be inherited by specific API clients.
It handles session management and common configuration.
"""

import os
from typing import Optional

import requests
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


class BaseClient:
    """
    Base API client with session management.

    This class provides common functionality for all API clients including:
        - Automatic session creation and management
        - Common headers configuration
        - Proper resource cleanup
    """

    def __init__(self, endpoint: str) -> None:
        """
        Initialize the base client.

        Args:
            endpoint: API endpoint path (e.g., 'register', 'users', 'products').
                     Will be appended to BASE_URL from environment variables.
        """
        self.endpoint = f"{os.getenv('BASE_URL')}{endpoint}"
        self._session: Optional[requests.Session] = None

    @property
    def session(self) -> requests.Session:
        """
        Get or create HTTP session with lazy initialization.

        Creates a new session on first access and configures default headers.
        Subsequent calls return the existing session.

        Returns:
            Configured requests.Session instance.
        """
        if self._session is None:
            self._session = requests.Session()
            self._session.headers.update({"Content-Type": "application/json"})
        return self._session

    def close_session(self) -> None:
        """
        Close the session and release resources.

        Should be called when the client is no longer needed to properly
        close HTTP connections and free resources.
        """
        if self._session is not None:
            self._session.close()
            self._session = None
