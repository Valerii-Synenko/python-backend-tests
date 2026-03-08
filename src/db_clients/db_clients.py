from db_clients.mongo.carts_client import CartsClient
from src.db_clients.mongo.orders_client import OrdersMongo
from src.db_clients.mongo.users_client import UsersMongo


class MongoClients:
    def __init__(self):
        self.users_db = UsersMongo()
        self.orders_db = OrdersMongo()
        self.carts_db = CartsClient()

    def close_connection(self):
        self.users_db.close_connection()
        self.orders_db.close_connection()
        self.carts_db.close_connection()


# TODO: add MS db client here


class DbClients:
    def __init__(self):
        self.mongo = MongoClients()
        # TODO: add ms_db object here

    def close_connection(self):
        self.mongo.close_connection()
