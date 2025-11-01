import pytest
from fastapi.testclient import TestClient

from fapi_tmpl.api.main import app
from fapi_tmpl.dependencies import get_app_settings

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_settings_cache():
    get_app_settings.cache_clear()
    yield
    get_app_settings.cache_clear()


def test_say_hello_default(monkeypatch):
    monkeypatch.delenv("FAPI_TMPL_USE_MOCK_GREETING", raising=False)
    response = client.get("/hello/Alice")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alice"}


def test_say_hello_with_mock_toggle(monkeypatch):
    monkeypatch.setenv("FAPI_TMPL_USE_MOCK_GREETING", "true")
    response = client.get("/hello/World")
    assert response.status_code == 200
    assert response.json() == {"message": "[mock] Hello, World"}
