# tests/sdk/test_fapi_tmpl_client.py
"""Tests for the fapi-tmpl SDK clients."""
from typing import Any, Dict

import httpx
import pytest
from fapi_tmpl_sdk.fapi_tmpl_client import FapiTmplClient, MockFapiTmplClient


class MockHttpxResponse:
    def __init__(self, json_data: Dict[str, Any], status_code: int = 200):
        self._json_data = json_data
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise httpx.HTTPStatusError(
                f"HTTP {self.status_code}", request=None, response=self
            )

    def json(self):
        return self._json_data


def test_client_get_health(monkeypatch):
    """FapiTmplClient should make a GET request to the /health endpoint."""
    captured = {}

    def fake_get(self, url: str):
        captured["url"] = url
        return MockHttpxResponse({"status": "ok"})

    monkeypatch.setattr("httpx.Client.get", fake_get)

    client = FapiTmplClient(base_url="http://test.com")
    response = client.get_health()

    assert captured["url"] == "http://test.com/health"
    assert response == {"status": "ok"}


def test_client_get_health_error(monkeypatch):
    """FapiTmplClient should raise RuntimeError on HTTP errors."""

    def fake_get(self, url: str):
        return MockHttpxResponse({}, status_code=500)

    monkeypatch.setattr("httpx.Client.get", fake_get)

    client = FapiTmplClient(base_url="http://test.com")
    with pytest.raises(RuntimeError, match="Failed to retrieve health status"):
        client.get_health()


def test_mock_client_get_health():
    """MockFapiTmplClient should return a canned response."""
    client = MockFapiTmplClient()
    response = client.get_health()
    assert response == {"status": "ok-mock"}
