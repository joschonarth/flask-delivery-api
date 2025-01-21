from src.use_cases.registry_deleter import RegistryDeleter
from src.models.repositories.orders_repository import OrdersRepository
from src.models.connection.connectio_handler import db_connection_handler

def registry_deleter_composer():
    conn = db_connection_handler.get_db_connection()
    model = OrdersRepository(conn)
    use_case = RegistryDeleter(model)

    return use_case
