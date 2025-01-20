from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError

def registry_updater_validator(body: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "customer": { "type": "string" },
                "items": {
                    "type": "list", "schema": {
                        "type": "dict",
                        "schema": {
                            "name": { "type": "string" },
                            "quantity": { "type": "integer", "min": 1 }
                        }
                    }
                },
                "total": { "type": "float", "min": 0.0 },
                "shipped": { "type": "boolean" }
            }
        }
    })
    response = body_validator.validate(body)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
