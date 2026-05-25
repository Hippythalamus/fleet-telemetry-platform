from fleet_telemetry_platform.orm_database import (
    insert_telemetry,
    get_all_telemetry,
)


insert_telemetry(
    robot_id="robot_1",
    battery=84.5,
    temperature=42.0,
)

packets = get_all_telemetry()

for packet in packets:
    print(packet.robot_id)
    print(packet.battery)
    print(packet.temperature)