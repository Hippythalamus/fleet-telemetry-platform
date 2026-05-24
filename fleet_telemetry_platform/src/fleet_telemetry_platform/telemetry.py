from dataclasses import dataclass
from typing import Generator
import random
import time


@dataclass
class TelemetryPacket:
    robot_id: str
    timestamp: float
    battery: float
    temperature: float
    position_x: float
    position_y: float


def telemetry_stream() -> Generator[TelemetryPacket, None, None]:
    robot_ids = ["robot_1", "robot_2", "robot_3"]

    while True:
        packet = TelemetryPacket(
            robot_id=random.choice(robot_ids),
            timestamp=time.time(),
            battery=round(random.uniform(20, 100), 2),
            temperature=round(random.uniform(30, 80), 2),
            position_x=round(random.uniform(0, 100), 2),
            position_y=round(random.uniform(0, 100), 2),
        )

        yield packet
