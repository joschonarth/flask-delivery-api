from src.main.http_types.http_request import HttpRequest
from .registry_order import RegistryOrder

class OrdersRepositoryMock:
    def __init__(self) -> None:
        self.insert_document_att = {}

    def insert_document(self, document: dict) -> None:
        self.insert_document_att["document"] = document

class OrdersRepositoryMockError:
    def insert_document(self, document: dict) -> None:
        raise Exception("Failed to insert document into repository")

def test_registry():
    repo = OrdersRepositoryMock()
    registry_order = RegistryOrder(repo)

    mock_registry = HttpRequest(
        body={
            "data": {
                "order_id": "123",
                "items": ["item1", "item2"],
                "total": 100.0
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert repo.insert_document_att["document"]["order_id"] == "123"
    assert repo.insert_document_att["document"]["items"] == ["item1", "item2"]
    assert repo.insert_document_att["document"]["total"] == 100.0
    assert "created_at" in repo.insert_document_att["document"]
    assert response.status_code == 201
    assert response.body == {
        "data": {
            "type": "Order",
            "count": 1,
            "registry": True
        }
    }

def test_registry_with_error():
    repo = OrdersRepositoryMockError()
    registry_order = RegistryOrder(repo)

    mock_registry = HttpRequest(
        body={
            "data": {
                "order_id": "123",
                "items": ["item1", "item2"],
                "total": 100.0
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert response.status_code == 400
    assert "error" in response.body
