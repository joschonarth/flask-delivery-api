from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError

def registry_order_validator(body: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "customer": { "type": "string", "required": True },
                "items": {
                    "type": "list", "required": True, "schema": {
                        "type": "dict",
                        "schema": {
                            "name": { "type": "string", "required": True },
                            "quantity": { "type": "integer", "required": True, "min": 1 }
                        }
                    }
                },
                "total": { "type": "float", "required": True, "min": 0.0 },
                "shipped": { "type": "boolean", "required": True }
            }
        }
    })
    response = body_validator.validate(body)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
