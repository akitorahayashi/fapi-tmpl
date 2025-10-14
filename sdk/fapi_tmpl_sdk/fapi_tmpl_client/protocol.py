# sdk/fapi_tmpl_sdk/fapi_tmpl_client/protocol.py
"""Defines the protocol for API clients interacting with the fapi-tmpl API."""
from typing import Any, Protocol


class FapiTmplClientProtocol(Protocol):
    """
    Protocol describing the interface for fapi-tmpl API clients.
    """

    def get_health(self) -> dict[str, Any]:
        """Retrieves the health status from the API."""
        ...
