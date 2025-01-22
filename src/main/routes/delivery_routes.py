from flask import Blueprint, jsonify, request, Response
from src.main.http_types.http_request import HttpRequest

from src.main.composer.registry_order_composer import registry_order_composer
from src.main.composer.registry_finder_composer import registry_finder_composer
from src.main.composer.registry_updater_composer import registry_updater_composer
from src.main.composer.registry_deleter_composer import registry_deleter_composer
from src.main.composer.registry_lister_composer import registry_lister_composer

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

@delivery_routes_bp.route("/delivery/order/<order_id>", methods=["DELETE"])
def delete_order(order_id):
    use_case = registry_deleter_composer()
    http_request = HttpRequest(path_params={ "order_id": order_id })
    use_case.delete(http_request)

    return Response(status=204)

@delivery_routes_bp.route("/delivery/orders", methods=["GET"])
def list_orders():
    use_case = registry_lister_composer()
    http_request = HttpRequest(query=request.args.to_dict())
    response = use_case.list(http_request)

    return jsonify(response.body), response.status_code
