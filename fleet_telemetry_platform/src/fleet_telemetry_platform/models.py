from pydantic import BaseModel


class TelemetryResponse(BaseModel):
    robot_id: str
    battery: float
    temperature: float


class RobotStatus(BaseModel):
    robot_id: str
    status: str
    battery: float


class TelemetryHistoryItem(BaseModel):
    robot_id: str
    timestamp: float
    battery: float
    temperature: float


class RobotCreateRequest(BaseModel):
    robot_id: str
    robot_type: str


class RobotCreateResponse(BaseModel):
    message: str
    robot_id: str


class TelemetryCreateRequest(BaseModel):
    robot_id: str
    battery: float
    temperature: float


class TelemetryCreateResponse(BaseModel):
    message: str
    robot_id: str
