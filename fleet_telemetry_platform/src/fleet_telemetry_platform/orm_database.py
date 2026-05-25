from fleet_telemetry_platform.orm_models import (
    SessionLocal,
    TelemetryORM,
)


def insert_telemetry(
    robot_id: str,
    battery: float,
    temperature: float,
):
    session = SessionLocal()

    telemetry = TelemetryORM(
        robot_id=robot_id,
        battery=battery,
        temperature=temperature,
    )

    session.add(telemetry)

    session.commit()

    session.close()

def get_all_telemetry():
    session = SessionLocal()

    telemetry_packets = session.query(
        TelemetryORM
    ).all()

    session.close()

    result = []

    for packet in telemetry_packets:
        result.append(
            {
                "robot_id": packet.robot_id,
                "battery": packet.battery,
                "temperature": packet.temperature,
            }
        )

    return result