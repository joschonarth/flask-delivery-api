from src.use_cases.registry_lister import RegistryLister
from src.models.repositories.orders_repository import OrdersRepository
from src.models.connection.connectio_handler import db_connection_handler

def registry_lister_composer():
    conn = db_connection_handler.get_db_connection()
    model = OrdersRepository(conn)
    use_case = RegistryLister(model)

    return use_case
