import sqlite3


DATABASE_NAME = "telemetry.db"

def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            robot_id TEXT,
            battery REAL,
            temperature REAL
        )
        """
    )
    connection.commit()
    connection.close()

def insert_telemetry(
    robot_id: str,
    battery: float,
    temperature: float,
):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO telemetry (
            robot_id,
            battery,
            temperature
        )
        VALUES (?, ?, ?)
        """,
        (
            robot_id,
            battery,
            temperature,
        ),
    )

    connection.commit()

    connection.close()

def get_all_telemetry():
    connection = get_connection()

    cursor = connection.cursor()

    rows = cursor.execute(
        """
        SELECT robot_id, battery, temperature
        FROM telemetry
        """
    ).fetchall()

    connection.close()

    result = []

    for row in rows:
        result.append(
            {
                "robot_id": row[0],
                "battery": row[1],
                "temperature": row[2],
            }
        )

    return result