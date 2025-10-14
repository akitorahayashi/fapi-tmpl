# tests/sdk/test_fapi_tmpl_client.py
"""Tests for the fapi-tmpl SDK clients."""
from typing import Any, Dict

from fapi_tmpl_sdk.fapi_tmpl_client import FapiTmplClient, MockFapiTmplClient


class MockHttpxResponse:
    def __init__(self, json_data: Dict[str, Any]):
        self._json_data = json_data

    def raise_for_status(self):
        pass

    def json(self):
        return self._json_data


def test_client_get_health(monkeypatch):
    """FapiTmplClient should make a GET request to the /health endpoint."""
    captured = {}

    def fake_get(url: str):
        captured["url"] = url
        return MockHttpxResponse({"status": "ok"})

    monkeypatch.setattr("httpx.get", fake_get)

    client = FapiTmplClient(base_url="http://test.com")
    response = client.get_health()

    assert captured["url"] == "http://test.com/health"
    assert response == {"status": "ok"}


def test_mock_client_get_health():
    """MockFapiTmplClient should return a canned response."""
    client = MockFapiTmplClient()
    response = client.get_health()
    assert response == {"status": "ok-mock"}
