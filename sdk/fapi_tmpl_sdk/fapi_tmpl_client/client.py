# sdk/fapi_tmpl_sdk/fapi_tmpl_client/client.py
"""Concrete HTTP client for the fapi-tmpl API."""
from typing import TYPE_CHECKING, Any

import httpx

from .protocol import FapiTmplClientProtocol


class FapiTmplClient:
    """A client for interacting with the fapi-tmpl API."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self._client = httpx.Client(timeout=30.0)

    def get_health(self) -> dict[str, Any]:
        """Retrieves the health status from the API."""
        try:
            url = f"{self.base_url}/health"
            response = self._client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise RuntimeError(f"Failed to retrieve health status: {e}") from e

    def close(self) -> None:
        """Closes the underlying HTTPX client."""
        self._client.close()

    def __enter__(self) -> "FapiTmplClient":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()


if TYPE_CHECKING:
    # Verify that the class implements the protocol
    _: FapiTmplClientProtocol = FapiTmplClient(base_url="")
