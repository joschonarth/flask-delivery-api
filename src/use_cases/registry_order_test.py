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
                "order_id": 1,
                "customer": "John Doe",
                "items": [
                    {"name": "Laptop", "quantity": 1},
                    {"name": "Keyboard", "quantity": 1}
                ],
                "total": 900.00,
                "shipped": True
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert repo.insert_document_att["document"]["order_id"] == 1
    assert repo.insert_document_att["document"]["customer"] == "John Doe"
    assert repo.insert_document_att["document"]["items"] == [
        {"name": "Laptop", "quantity": 1},
        {"name": "Keyboard", "quantity": 1}
    ]
    assert repo.insert_document_att["document"]["total"] == 900.00
    assert repo.insert_document_att["document"]["shipped"] is True
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
                "order_id": 1,
                "customer": "John Doe",
                "items": [
                    {"name": "Laptop", "quantity": 1},
                    {"name": "Keyboard", "quantity": 1}
                ],
                "total": 900.00,
                "shipped": True
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert response.status_code == 400
    assert "error" in response.body
