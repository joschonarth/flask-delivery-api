import pytest
from src.models.connection.connectio_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="interaction with the database")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"order_id": 1, "customer": "John Doe", "items": ["Laptop"], "total": 900.00, "shipped": True}
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="interaction with the database")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [
        {"order_id": 2, "customer": "Alice Smith", "items": ["Keyboard"], "total": 120.50, "shipped": False},
        {"order_id": 3, "customer": "Bob Johnson", "items": ["Mouse"], "total": 25.99, "shipped": True},
        {"order_id": 4, "customer": "Emma Brown", "items": ["Headphones"], "total": 80.30, "shipped": False}
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