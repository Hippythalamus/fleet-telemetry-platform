import asyncio
import random

async def telemetry_worker(robot_id: str):
    while True:
        battery = round(random.uniform(20, 100), 2)

        print(f"{robot_id}: battery={battery}")

        await asyncio.sleep(1)




async def main():
    await asyncio.gather(
        telemetry_worker("robot 1"),
        telemetry_worker("robot 2"),
        telemetry_worker("robot 3"),
    )

asyncio.run(main())