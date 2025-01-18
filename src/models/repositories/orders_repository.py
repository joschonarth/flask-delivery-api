from bson.objectid import ObjectId

class OrdersRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data

    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
        return response

    def select_many_with_properties(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter,
            { "_id": 0, "order_id": 0, "total": 0, "shipped": 0 }
        )
        return data

    def select_if_property_exists(self,) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find(
            { "address": { "$exists": True } },
            { "_id": 0, "order_id": 0, "total": 0, "shipped": 0 }
        )
        return response

    def select_by_object_id(self, object_id: str) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({ "_id": ObjectId(object_id) })
        return data

    def edit_registry(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id": ObjectId(object_id) },
            { "$set": { "total": 1000 } }
        )

    def edit_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            { "shipped": False },
            { "$set": {"shipped": True } }
        )

    def edit_registry_with_increment(self, object_id: str, item_name: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id": ObjectId(object_id), "items.name": item_name },
            { "$inc": { "items.$.quantity": 1 } }
        )

    def delete_registry(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({ "_id": ObjectId(object_id) })

    def delete_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many({ "shipped": True })
