from typing import Any

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.results import InsertOneResult

load_dotenv()


class _CollectionWrapper:
    """
    Wrapper for MongoDB collection. This wrapper is applicable for the working with context of one collection.
    """

    def __init__(self, collection):
        self._collection = collection

    def find_one(self, query: dict[str, Any]) -> dict[str, Any] | None:
        """
        Find one document in the given collection.

        Args:
            query: The query to find the document.

        Returns:
            Found document or None if the document doesn't exist.

        """
        return self._collection.find_one(query)

    def insert_one(self, document: dict[str, Any]) -> InsertOneResult:
        """
        Insert one document into the given collection.
        Args:
            document: The document to insert.

        Returns:
            InsertOneResult: Object containing metadata about the operation,
            including the inserted document ID (inserted_id).

        """
        return self._collection.insert_one(document)

    def delete_one(self, query: dict[str, Any]) -> int:
        """
        Delete one document matching the query.

        Args:
            query: The query to find the document.

        Returns:
            Number of deleted documents (0 or 1).

        """
        return self._collection.delete_one(query).deleted_count

    def delete_many(self, query: dict[str, Any]) -> int:
        """
        Delete one or more documents matching the query.

        Args:
            query: The query to find the documents.

        Returns:
            Number of deleted documents (0 or more).

        """
        return self._collection.delete_many(query).deleted_count


class BaseMongoClient:
    """
    Base class for all MongoDB clients.
    """

    def __init__(self, host: str, port: int, db_name: str):
        if not host or not port or not db_name:
            raise RuntimeError(
                f"Cannot create Mongo client. \nhost={host}, \nport={port}, \ndb_name={db_name}"
            )

        self._client = MongoClient(host=host, port=port)
        self._db: Database = self._client[db_name]
        self._collections_cache: dict[Any, _CollectionWrapper] = {}

    def close(self) -> None:
        """
        Close the MongoDB client.
        """
        self._client.close()

    def get_collection(self, name: str) -> _CollectionWrapper:
        """
        Returns a collection wrapper for by the given name.
        Args:
            name: The name of the collection you want to get a collection wrapper for.

        Returns: The collection wrapper by the given name.

        Raises: `ValueError` if you try to get a collection wrapper that doesn't exist.

        """
        existing_collections = self._db.list_collection_names()
        if name not in existing_collections:
            raise ValueError(f"Collection '{name}' does not exist in db '{self._db.name}'")

        if name not in self._collections_cache:
            self._collections_cache[name] = _CollectionWrapper(self._db[name])
        return self._collections_cache[name]
