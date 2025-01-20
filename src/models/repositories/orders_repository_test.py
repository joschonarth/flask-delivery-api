from bson.objectid import ObjectId
from .orders_repository import OrdersRepository

class CollectionMock:
    def __init__(self) -> None:
        self.insert_one_attributes = {}
        self.insert_many_attributes = {}
        self.find_attributes = {}
        self.find_one_attributes = {}
        self.update_one_attributes = {}
        self.update_many_attributes = {}
        self.delete_one_attributes = {}
        self.delete_many_attributes = {}

    def insert_one(self, input_data: any):
        self.insert_one_attributes["dict"] = input_data

    def insert_many(self, input_data: any):
        self.insert_many_attributes["list"] = input_data

    def find(self, *args):
        self.find_attributes["args"] = args

    def find_one(self, doc_filter):
        self.find_one_attributes["doc_filter"] = doc_filter
        return {"_id": doc_filter["_id"]}

    def update_one(self, doc_filter, update):
        self.update_one_attributes["doc_filter"] = doc_filter
        self.update_one_attributes["update"] = update

    def update_many(self, doc_filter, update):
        self.update_many_attributes["doc_filter"] = doc_filter
        self.update_many_attributes["update"] = update

    def delete_one(self, doc_filter):
        self.delete_one_attributes["doc_filter"] = doc_filter

    def delete_many(self, doc_filter):
        self.delete_many_attributes["doc_filter"] = doc_filter

class DbCollectionMock:
    def __init__(self, collection) -> None:
        self.get_collection_attributes = {}
        self.collection = collection

    def get_collection(self, collection_name):
        self.get_collection_attributes["name"] = collection_name
        return self.collection

def test_insert_document():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc = { "test": "insert" }
    repo.insert_document(doc)

    assert collection.insert_one_attributes["dict"] == doc

def test_insert_list_of_documents():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    docs = [{"test": "insert1"}, {"test": "insert2"}]
    repo.insert_list_of_documents(docs)

    assert collection.insert_many_attributes["list"] == docs

def test_select_many():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc_filter = { "test": "find" }
    repo.select_many(doc_filter)

    assert collection.find_attributes["args"][0] == doc_filter

def test_select_one():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc_filter = { "_id": ObjectId("60b725f10c9ac7472f3d8d52") }
    result = repo.select_one(doc_filter)

    assert collection.find_one_attributes["doc_filter"] == doc_filter
    assert result == {"_id": doc_filter["_id"]}

def test_select_many_with_properties():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc_filter = { "test": "find" }
    repo.select_many_with_properties(doc_filter)

    assert collection.find_attributes["args"][0] == doc_filter
    assert collection.find_attributes["args"][1] == {'_id': 0, 'order_id': 0, 'total': 0, 'shipped': 0}

def test_edit_registry():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    object_id = "60b725f10c9ac7472f3d8d52"
    update_fields = {"total": 1000}

    repo.edit_registry(object_id, update_fields)

    assert collection.update_one_attributes["doc_filter"] == {"_id": ObjectId(object_id)}
    assert collection.update_one_attributes["update"] == {"$set": update_fields}

def test_edit_many_registries():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    repo.edit_many_registries()

    assert collection.update_many_attributes["doc_filter"] == {"shipped": False}
    assert collection.update_many_attributes["update"] == {"$set": {"shipped": True}}

def test_delete_registry():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    object_id = "60b725f10c9ac7472f3d8d52"
    repo.delete_registry(object_id)

    assert collection.delete_one_attributes["doc_filter"] == {"_id": ObjectId(object_id)}

def test_delete_many_registries():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    repo.delete_many_registries()

    assert collection.delete_many_attributes["doc_filter"] == {"shipped": True}
