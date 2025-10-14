"""fapi-tmpl SDK client module."""

from .client import FapiTmplClient
from .mock import MockFapiTmplClient
from .protocol import FapiTmplClientProtocol

__all__ = ["FapiTmplClientProtocol", "FapiTmplClient", "MockFapiTmplClient"]
