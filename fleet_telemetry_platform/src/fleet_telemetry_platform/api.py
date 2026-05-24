from fastapi import FastAPI
import time
from fleet_telemetry_platform.models import (
    TelemetryResponse,
    RobotStatus,
    TelemetryHistoryItem,
    RobotCreateRequest,
    RobotCreateResponse,
)
from fleet_telemetry_platform.models import (
    TelemetryCreateRequest,
    TelemetryCreateResponse,
)
from fleet_telemetry_platform.telemetry import telemetry_stream

app = FastAPI()

stream = telemetry_stream()


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Telemetry API is running"}


@app.post("/robots", response_model=RobotCreateResponse)
def create_robot(robot: RobotCreateRequest) -> RobotCreateResponse:
    return RobotCreateResponse(
        message="Robot created successfully", robot_id=robot.robot_id
    )


@app.post("/telemetry/save", response_model=TelemetryCreateResponse)
def save_telemetry(robot: TelemetryCreateRequest) -> TelemetryCreateResponse:
    return TelemetryCreateResponse(
        message="Robot's telemetry was saved successfully", robot_id=robot.robot_id
    )


@app.get("/telemetry/latest", response_model=TelemetryResponse)
def latest_telemetry() -> TelemetryResponse:
    packet = next(stream)

    return TelemetryResponse(
        robot_id=packet.robot_id,
        battery=packet.battery,
        temperature=packet.temperature,
    )


@app.get("/telemetry/status", response_model=list[RobotStatus])
def latest_status() -> list[RobotStatus]:

    return [
        RobotStatus(robot_id="robot_1", status="online", battery=84.2),
        RobotStatus(robot_id="robot_2", status="offline", battery=12.5),
    ]


@app.get("/telemetry/history", response_model=list[TelemetryHistoryItem])
def telemetry_history() -> list[TelemetryHistoryItem]:
    return [
        TelemetryHistoryItem(
            robot_id="robot_1", temperature=42.1, timestamp=time.time(), battery=84.5
        ),
        TelemetryHistoryItem(
            robot_id="robot_2", timestamp=time.time(), temperature=43.5, battery=12.5
        ),
    ]


@app.get("/hello")
def hello(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}"}


@app.get("/echo")
def echo(message: str) -> dict[str, str]:
    return {"message": message}
