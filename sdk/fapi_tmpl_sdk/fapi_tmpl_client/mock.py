# sdk/fapi_tmpl_sdk/fapi_tmpl_client/mock.py
"""Mock implementation of the fapi-tmpl API client for testing."""
from typing import Any

from .protocol import FapiTmplClientProtocol


class MockFapiTmplClient:
    """Mock client that returns canned responses for the fapi-tmpl API."""

    def get_health(self) -> dict[str, Any]:
        """Returns a fixed health status payload."""
        print("MockFapiTmplClient.get_health() called")
        return {"status": "ok-mock"}


# Verify that the class implements the protocol
_: FapiTmplClientProtocol = MockFapiTmplClient()
