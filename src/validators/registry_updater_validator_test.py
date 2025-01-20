import pytest
from .registry_updater_validator import registry_updater_validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError

def test_registry_updater_validator():
    body = {
        "data": {
            "customer": "John Doe",
            "items": [
                {"name": "Laptop", "quantity": 2},
                {"name": "Mouse", "quantity": 1}
            ],
            "total": 1200.50,
            "shipped": False
        }
    }
    registry_updater_validator(body)

def test_registry_updater_validator_with_invalid_quantity():
    body_with_error = {
        "data": {
            "customer": "John Doe",
            "items": [
                {"name": "Laptop", "quantity": 0}
            ],
            "total": 1200.50,
            "shipped": False
        }
    }
    with pytest.raises(HttpUnprocessableEntityError):
        registry_updater_validator(body_with_error)

def test_registry_updater_validator_with_negative_total():
    body_with_error = {
        "data": {
            "customer": "John Doe",
            "items": [
                {"name": "Laptop", "quantity": 1}
            ],
            "total": -100.00,
            "shipped": False
        }
    }
    with pytest.raises(HttpUnprocessableEntityError):
        registry_updater_validator(body_with_error)

def test_registry_updater_validator_with_invalid_data_type():
    body_with_error = {
        "data": {
            "customer": 12345,
            "items": [
                {"name": "Laptop", "quantity": 1}
            ],
            "total": 1200.50,
            "shipped": False
        }
    }
    with pytest.raises(HttpUnprocessableEntityError):
        registry_updater_validator(body_with_error)
