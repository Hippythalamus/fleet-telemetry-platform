from fleet_telemetry_platform.telemetry import telemetry_stream
from fleet_telemetry_platform.json_demo import json_searilazion


def main() -> None:
    stream = telemetry_stream()
    json_searilazion()
    for _ in range(5):
        packet = next(stream)
        print(packet)


if __name__ == "__main__":
    main()
