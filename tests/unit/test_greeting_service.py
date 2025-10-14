"""Unit tests for the greeting service."""

from fapi_tmpl.services.greeting_service import GreetingService


def test_greeting_service_generate_greeting():
    service = GreetingService()
    result = service.generate_greeting("World")
    assert result == "Hello, World"
