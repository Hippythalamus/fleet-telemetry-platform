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