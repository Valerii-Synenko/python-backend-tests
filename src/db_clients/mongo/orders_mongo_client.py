import os

from dotenv import load_dotenv

from db_clients.mongo.base_mongo_client import BaseMongoClient

load_dotenv()


class OrdersMongo(BaseMongoClient):
    def __init__(self):
        super().__init__(
            host=os.getenv("MONGO_DB_HOST"),
            port=int(os.getenv("ORDERS_DB_PORT")),
            db_name=os.getenv("ORDERS_DB_NAME"),
        )

    @property
    def customer_order(self):
        """Returns the customer_order collection wrapper"""
        return self.get_collection("customerOrder")
