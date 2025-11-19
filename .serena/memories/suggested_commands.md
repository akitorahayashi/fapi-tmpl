# Suggested Commands
- `just setup` – install dependencies with uv and scaffold `.env`.
- `just dev` – run FastAPI app locally with reload via uvicorn.
- `just up` / `just down` – start/stop Docker Compose environment.
- `just test` – run unit, integration, e2e suites plus docker build smoke.
- `just check` / `just fix` – check or autofix code style with ruff.
- `uv run pytest tests/unit -k <pattern>` – targeted test execution when debugging.