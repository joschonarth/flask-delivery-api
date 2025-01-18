import pytest
from src.models.connection.connectio_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="interaction with the database")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"order_id": 1, "customer": "John Doe", "items": [{"name": "Laptop", "quantity": 1}, {"name": "Keyboard", "quantity": 1}], "total": 900.00, "shipped": True}
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="interaction with the database")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [
        {"order_id": 2, "customer": "Alice Smith", "items": [{"name": "Keyboard", "quantity": 1}], "total": 120.50, "shipped": False},
        {"order_id": 3, "customer": "Bob Johnson", "items": [{"name": "Mouse", "quantity": 1}], "total": 25.99, "shipped": True},
        {"order_id": 4, "customer": "Emma Brown", "items": [{"name": "Headphones", "quantity": 2}], "total": 80.30, "shipped": False},
        {"order_id": 5, "customer": "David Wilson", "items": [{"name": "Monitor", "quantity": 1}], "total": 450.00, "shipped": True}
    ]
    orders_repository.insert_list_of_documents(my_doc)

@pytest.mark.skip(reason="interaction with the database")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "shipped": True }
    response = orders_repository.select_many(doc_filter)
    print(response)
    for doc in response:
        print(doc)

@pytest.mark.skip(reason="interaction with the database")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "shipped": True }
    response = orders_repository.select_one(doc_filter)
    print(response)

@pytest.mark.skip(reason="interaction with the database")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "shipped": True }
    response = orders_repository.select_many_with_properties(doc_filter)
    print(response)
    for doc in response:
        print(doc)

@pytest.mark.skip(reason="interaction with the database")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()
    print(response)
    for doc in response:
        print(doc)

@pytest.mark.skip(reason="interaction with the database")
def test_select_many_with_multiple_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "shipped": True,
        "items.name": "Laptop"
    }
    response = orders_repository.select_many(doc_filter)
    for doc in response:
        print(doc)

@pytest.mark.skip(reason="interaction with the database")
def test_select_many_with_or_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [
            {"shipped": True},
            {"items.quantity": 2}
        ]
    }
    response = orders_repository.select_many(doc_filter)
    for doc in response:
        print(doc)

@pytest.mark.skip(reason="interaction with the database")
def test_select_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "678ae9ddc62fca13b6e23dd3"
    response = orders_repository.select_by_object_id(object_id)
    print(f"\n{response}")

@pytest.mark.skip(reason="interaction with the database")
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    object_id = "678aea30acd432c259ed0453"
    orders_repository.edit_registry(object_id)

@pytest.mark.skip(reason="interaction with the database")
def test_edit_many_registries():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_many_registries()

@pytest.mark.skip(reason="interaction with the database")
def test_edit_registry_with_increment():
    orders_repository = OrdersRepository(conn)
    object_id = "678aea30acd432c259ed0453"
    item_name = "Laptop"
    orders_repository.edit_registry_with_increment(object_id, item_name)
