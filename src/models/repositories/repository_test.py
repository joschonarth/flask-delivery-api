from src.models.connection.connectio_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"order_id": 1, "customer": "John Doe", "items": ["Laptop"], "total": 900.00}
    orders_repository.insert_document(my_doc)

def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [
        {"order_id": 2, "customer": "Alice Smith", "items": ["Keyboard"], "total": 120.50},
        {"order_id": 3, "customer": "Bob Johnson", "items": ["Mouse"], "total": 25.99},
        {"order_id": 4, "customer": "Emma Brown", "items": ["Headphones"], "total": 80.30}
    ]
    orders_repository.insert_list_of_documents(my_doc)
