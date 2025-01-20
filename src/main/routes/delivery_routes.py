from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest

from src.main.composer.registry_order_composer import registry_order_composer
from src.main.composer.registry_finder_composer import registry_finder_composer
from src.main.composer.registry_updater_composer import registry_updater_composer

delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def create_order():
    use_case = registry_order_composer()
    http_request = HttpRequest(body=request.json)
    response = use_case.registry(http_request)

    return jsonify(response.body), response.status_code

@delivery_routes_bp.route("/delivery/order/<order_id>", methods=["GET"])
def get_order(order_id):
    use_case = registry_finder_composer()
    http_request = HttpRequest(path_params={ "order_id": order_id })
    response = use_case.find(http_request)

    return jsonify(response.body), response.status_code

@delivery_routes_bp.route("/delivery/order/<order_id>", methods=["PATCH"])
def update_order(order_id):
    use_case = registry_updater_composer()
    http_request = HttpRequest(
        path_params={ "order_id": order_id },
        body=request.json
    )
    response = use_case.update(http_request)

    return jsonify(response.body), response.status_code
