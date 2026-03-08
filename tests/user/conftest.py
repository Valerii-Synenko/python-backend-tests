import pytest
from pymongo.results import InsertOneResult


@pytest.fixture(scope="function")
def insert_user_to_mongo(db_client):
    address = {
        "number": "123",
        "street": "Main Street",
        "city": "London",
        "postcode": "SW1A 1AA",
        "country": "United Kingdom",
    }

    address_result: InsertOneResult = db_client.mongo.users_db.addresses_collection.insert_one(
        address
    )

    card = {
        "longNum": "1234567890123456",
        "expires": "12/27",
        "ccv": "123",
    }

    card_result: InsertOneResult = db_client.mongo.users_db.cards_collection.insert_one(card)

    customer = {
        "firstName": "Valerij",
        "lastName": "Synenko",
        "username": "John_Doe",
        "password": "hashed_password",
        "salt": "some_salt",
        "addresses": [address_result.inserted_id],
        "cards": [card_result.inserted_id],
    }

    customer_result: InsertOneResult = db_client.mongo.users_db.customers_collection.insert_one(
        customer
    )
    print("customer_result.inserted_id: ", customer_result.inserted_id)

    yield customer_result

    print("customer_result.inserted_id: ", customer_result.inserted_id)

    db_client.mongo.users_db.addresses_collection.delete_one({"_id": address_result.inserted_id})
    db_client.mongo.users_db.cards_collection.delete_one({"_id": card_result.inserted_id})
    db_client.mongo.users_db.customers_collection.delete_one({"_id": customer_result.inserted_id})
