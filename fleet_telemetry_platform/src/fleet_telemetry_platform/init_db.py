from fleet_telemetry_platform.database import (
    create_table,
    insert_test_data,
    get_all_telemetry,
)


create_table()
print("Database initialized")

insert_test_data()

rows = get_all_telemetry()

print(rows)