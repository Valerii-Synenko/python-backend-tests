import os

from dotenv import load_dotenv

from db_clients.mongo.base_client import BaseMongoClient

load_dotenv()


class UsersMongo(BaseMongoClient):
    def __init__(self):
        super().__init__(
            host=os.getenv("MONGO_DB_HOST"),
            port=int(os.getenv("USERS_DB_PORT")),
            db_name=os.getenv("USERS_DB_NAME"),
        )

    @property
    def customers_collection(self):
        """Returns the customers collection wrapper."""
        return self.get_collection("customers")

    @property
    def addresses_collection(self):
        """Returns the addresses collection wrapper."""
        return self.get_collection("addresses")

    @property
    def cards_collection(self):
        """Returns the cards collection wrapper."""
        return self.get_collection("cards")
