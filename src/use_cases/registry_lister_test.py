from src.main.http_types.http_request import HttpRequest
from src.use_cases.registry_lister import RegistryLister

def test_list():
    class OrdersRepositoryMock:
        def select_many(self, filters: dict):
            _ = filters
            return [
                {"_id": 1, "customer": "John Doe", "total": 100.00},
                {"_id": 2, "customer": "Jane Doe", "total": 150.00}
            ]

    repo = OrdersRepositoryMock()
    registry_lister = RegistryLister(repo)

    mock_request = HttpRequest(query={})
    response = registry_lister.list(mock_request)

    assert response.status_code == 200
    assert response.body == {
        "data": [
            {"_id": "1", "customer": "John Doe", "total": 100.00},
            {"_id": "2", "customer": "Jane Doe", "total": 150.00}
        ],
        "count": 2
    }

def test_list_with_filters():
    class OrdersRepositoryMock:
        def select_many(self, filters: dict):
            if filters.get("customer") == "John Doe":
                return [
                    {"_id": 1, "customer": "John Doe", "total": 100.00}
                ]
            return [
                {"_id": 1, "customer": "John Doe", "total": 100.00},
                {"_id": 2, "customer": "Jane Doe", "total": 150.00}
            ]

    repo = OrdersRepositoryMock()
    registry_lister = RegistryLister(repo)

    mock_request = HttpRequest(query={"customer": "John Doe"})
    response = registry_lister.list(mock_request)

    assert response.status_code == 200
    assert response.body == {
        "data": [{"_id": "1", "customer": "John Doe", "total": 100.00}],
        "count": 1
    }

def test_list_with_error():
    class OrdersRepositoryMockError:
        def select_many(self, filters: dict):
            raise Exception("Database error")

    repo = OrdersRepositoryMockError()
    registry_lister = RegistryLister(repo)

    mock_request = HttpRequest(query={})
    response = registry_lister.list(mock_request)

    assert response.status_code == 500
    assert "errors" in response.body
    assert response.body["errors"][0]["detail"] == "Database error"
    assert response.body["errors"][0]["title"] == "Server Error"


def test_list_no_filters():
    class OrdersRepositoryMock:
        def select_many(self, filters: dict):
            _ = filters
            return [
                {"_id": 1, "customer": "John Doe", "total": 100.00},
                {"_id": 2, "customer": "Jane Doe", "total": 150.00}
            ]

    repo = OrdersRepositoryMock()
    registry_lister = RegistryLister(repo)

    mock_request = HttpRequest(query={})
    response = registry_lister.list(mock_request)

    assert response.status_code == 200
    assert response.body["count"] == 2
    assert len(response.body["data"]) == 2
