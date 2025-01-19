import pytest
from .registry_order_validator import registry_order_validator

def test_registry_order_validator():
    body = {
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
    registry_order_validator(body)

def test_registry_order_validator_with_error():
    body_with_error = {
        "data": {
            "order_id": "1",
            "customer": "John Doe",
            "items": [
                {"name": "Laptop", "quantity": 1},
                {"name": "Keyboard", "quantity": 1}
            ],
            "total": 900.00,
            "shipped": True
        }
    }
    with pytest.raises(Exception):
        registry_order_validator(body_with_error)
