from fastapi.testclient import TestClient

from fapi_tmpl.api.main import app  # Import app directly from main
from fapi_tmpl.dependencies import get_greeting_service
from fapi_tmpl.protocols.greeting_service_protocol import GreetingServiceProtocol

client = TestClient(app)


def test_say_hello_default():
    response = client.get("/hello/Alice")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alice"}


def test_say_hello_with_override():
    class MockGreetingService(GreetingServiceProtocol):
        def generate_greeting(self, name: str) -> str:
            return f"Goodbye, {name}"

    # Override the dependency
    app.dependency_overrides[get_greeting_service] = lambda: MockGreetingService()

    try:
        response = client.get("/hello/World")
        assert response.status_code == 200
        assert response.json() == {"message": "Goodbye, World"}
    finally:
        # Always clear the override
        app.dependency_overrides.clear()
