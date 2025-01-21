from src.models.repositories.interfaces.orders_repository import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.error_handler import error_handler

class RegistryDeleter:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def delete(self, http_request: HttpRequest) -> None:
        try:
            order_id = http_request.path_params["order_id"]
            self.__search_order(order_id)
            self.__delete_order(order_id)
        except Exception as exception:
            return error_handler(exception)

    def __search_order(self, order_id: str) -> dict:
        order = self.__orders_repository.select_by_object_id(order_id)
        if not order:
            raise HttpNotFoundError("Order not found")
        return order

    def __delete_order(self, order_id: str) -> None:
        self.__orders_repository.delete_registry(order_id)
