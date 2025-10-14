"""fapi-tmpl SDK package."""

from .fapi_tmpl_client import (
    FapiTmplClient,
    FapiTmplClientProtocol,
    MockFapiTmplClient,
)

__all__ = ["FapiTmplClientProtocol", "FapiTmplClient", "MockFapiTmplClient"]
