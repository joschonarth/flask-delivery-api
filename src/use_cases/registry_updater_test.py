from src.main.http_types.http_request import HttpRequest
from .registry_updater import RegistryUpdater

class OrdersRepositoryMock:
    def __init__(self) -> None:
        self.database = {
            "order_123": {
                "customer": "Ana",
                "items": [{"name": "Phone", "quantity": 1}],
                "total": 1500.00
            }
        }
        self.edit_registry_att = {}

    def select_by_object_id(self, order_id: str):
        return self.database.get(order_id)

    def edit_registry(self, order_id: str, update_field: dict):
        if order_id in self.database:
            self.database[order_id].update(update_field)
            self.edit_registry_att["order_id"] = order_id
            self.edit_registry_att["update_field"] = update_field

class OrdersRepositoryMockError:
    def select_by_object_id(self, order_id: str):
        _ = order_id
        return None

    def edit_registry(self, order_id: str, update_field: dict):
        raise Exception("Failed to update document in repository")

def test_update():
    repo = OrdersRepositoryMock()
    registry_updater = RegistryUpdater(repo)

    mock_update = HttpRequest(
        path_params={"order_id": "order_123"},
        body={
            "data": {
                "total": 600.00,
                "shipped": True
            }
        }
    )

    response = registry_updater.update(mock_update)

    assert repo.edit_registry_att["order_id"] == "order_123"
    assert repo.edit_registry_att["update_field"] == {"total": 600.00, "shipped": True}
    assert response.status_code == 200
    assert response.body == {
        "data": {
            "order_id": "order_123",
            "type": "Order",
            "count": 1
        }
    }

def test_update_not_found():
    repo = OrdersRepositoryMockError()
    registry_updater = RegistryUpdater(repo)

    mock_update = HttpRequest(
        path_params={"order_id": "invalid_id"},
        body={
            "data": {
                "total": 600.00
            }
        }
    )

    response = registry_updater.update(mock_update)

    assert response.status_code == 404
    assert "errors" in response.body

def test_update_with_error():
    repo = OrdersRepositoryMock()
    registry_updater = RegistryUpdater(repo)

    mock_update = HttpRequest(
        path_params={"order_id": "order_123"},
        body={
            "invalid_key": {
                "total": 600.00
            }
        }
    )

    response = registry_updater.update(mock_update)

    assert response.status_code == 422
    assert "errors" in response.body
