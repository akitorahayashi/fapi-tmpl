"""HTTP routes exposed by the FastAPI template."""

from fastapi import APIRouter, Depends

from ..dependencies import get_greeting_service
from ..protocols.greeting_service_protocol import GreetingServiceProtocol

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
    """Return a simple health status payload."""
    return {"status": "ok"}


@router.get("/hello/{name}")
async def say_hello(
    name: str,
    greeter: GreetingServiceProtocol = Depends(get_greeting_service),
) -> dict[str, str]:
    greeting = greeter.generate_greeting(name)
    return {"message": greeting}
