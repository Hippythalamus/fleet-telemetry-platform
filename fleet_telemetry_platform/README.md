# Fleet Telemetry Platform
Backend platform for robotic fleet telemetry, monitoring, and sensor data ingestion.
Educational backend project for learning:
- Modern Python tooling
- Type checking
- Linting
- Structured project layout
- Python backend development
- FastAPI
- REST APIs
- Pydantic
- Generators
- Telemetry streaming concepts

## Setup

```bash
uv sync run

uv run python src/fleet_telemetry_platform/main.py
```

## Run

```bash
export PYTHONPATH=src
uv run uvicorn fleet_telemetry_platform.api:app --reload