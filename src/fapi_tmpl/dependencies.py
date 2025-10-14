from functools import lru_cache

from .config import AppSettings
from .protocols.greeting_service_protocol import GreetingServiceProtocol
from .services.greeting_service import GreetingService


@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()


def get_greeting_service() -> GreetingServiceProtocol:
    return GreetingService()
