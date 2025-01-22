from src.models.repositories.interfaces.orders_repository import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler

class RegistryLister:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def list(self, http_request: HttpRequest) -> HttpResponse:
        try:
            filters = http_request.query if http_request.query else {}
            orders = self.__fetch_orders(filters)
            return self.__format_response(orders)
        except Exception as exception:
            return error_handler(exception)

    def __fetch_orders(self, filters: dict) -> list:
        return self.__orders_repository.select_many(filters)

    def __format_response(self, orders: list) -> HttpResponse:
        formatted_orders = []
        for order in orders:
            order["_id"] = str(order["_id"])
            formatted_orders.append(order)

        return HttpResponse(
            body={
                "data": formatted_orders,
                "count": len(formatted_orders)
            },
            status_code=200
        )
