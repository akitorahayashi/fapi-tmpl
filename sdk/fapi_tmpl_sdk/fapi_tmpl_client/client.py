# sdk/fapi_tmpl_sdk/fapi_tmpl_client/client.py
"""Concrete HTTP client for the fapi-tmpl API."""
from typing import Any

import httpx

from .protocol import FapiTmplClientProtocol


class FapiTmplClient:
    """A client for interacting with the fapi-tmpl API."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get_health(self) -> dict[str, Any]:
        """Retrieves the health status from the API."""
        url = f"{self.base_url}/health"
        response = httpx.get(url)
        response.raise_for_status()
        return response.json()


# Verify that the class implements the protocol
_: FapiTmplClientProtocol = FapiTmplClient(base_url="")
