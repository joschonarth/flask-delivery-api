from src.main.http_types.http_request import HttpRequest
from .registry_deleter import RegistryDeleter

class OrdersRepositoryMock:
    def __init__(self):
        self.database = {
            "order_123": {
                "customer": "Jane Doe",
                "items": [
                    {"name": "Mouse", "quantity": 1},
                    {"name": "Monitor", "quantity": 2}
                ],
                "total": 300.00,
                "shipped": False
            }
        }

    def select_by_object_id(self, order_id: str):
        return self.database.get(order_id)

    def delete_registry(self, order_id: str):
        if order_id in self.database:
            del self.database[order_id]


class OrdersRepositoryMockError:
    def select_by_object_id(self, order_id: str):
        _ = order_id
        return None

    def delete_registry(self, order_id: str):
        raise Exception("Failed to delete order")


def test_delete():
    repo = OrdersRepositoryMock()
    registry_deleter = RegistryDeleter(repo)

    mock_request = HttpRequest(path_params={"order_id": "order_123"})
    response = registry_deleter.delete(mock_request)

    assert response is None
    assert "order_123" not in repo.database


def test_delete_not_found():
    repo = OrdersRepositoryMockError()
    registry_deleter = RegistryDeleter(repo)

    mock_request = HttpRequest(path_params={"order_id": "invalid_order"})
    response = registry_deleter.delete(mock_request)

    assert response.status_code == 404
    assert "errors" in response.body
    assert response.body["errors"][0]["detail"] == "Order not found"
    assert response.body["errors"][0]["title"] == "Not Found"


def test_delete_with_error():
    repo = OrdersRepositoryMockError()
    registry_deleter = RegistryDeleter(repo)

    mock_request = HttpRequest(path_params={"order_id": "order_123"})
    response = registry_deleter.delete(mock_request)

    assert response.status_code == 404
    assert "errors" in response.body
    assert response.body["errors"][0]["detail"] == "Order not found"
    assert response.body["errors"][0]["title"] == "Not Found"
