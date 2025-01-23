from src.main.http_types.http_request import HttpRequest
from .registry_finder import RegistryFinder

def test_find():
    class OrdersRepositoryMock:
        def select_by_object_id(self, order_id: str):
            return {
                "_id": order_id,
                "customer": "Jane Doe",
                "items": [
                    {"name": "Mouse", "quantity": 1},
                    {"name": "Monitor", "quantity": 2}
                ],
                "total": 300.00,
                "shipped": False
            }

    repo = OrdersRepositoryMock()
    registry_finder = RegistryFinder(repo)

    mock_request = HttpRequest(path_params={"order_id": "12345"})
    response = registry_finder.find(mock_request)

    assert response.status_code == 200
    assert response.body == {
        "data": {
            "count": 1,
            "type": "Order",
            "attributes": {
                "_id": "12345",
                "customer": "Jane Doe",
                "items": [
                    {"name": "Mouse", "quantity": 1},
                    {"name": "Monitor", "quantity": 2}
                ],
                "total": 300.00,
                "shipped": False
            }
        }
    }

def test_find_with_error():
    class OrdersRepositoryMockError:
        def select_by_object_id(self, order_id: str):
            _ = order_id
            return None

    repo = OrdersRepositoryMockError()
    registry_finder = RegistryFinder(repo)

    mock_request = HttpRequest(path_params={"order_id": "54321"})
    response = registry_finder.find(mock_request)

    assert response.status_code == 404
    assert "errors" in response.body
