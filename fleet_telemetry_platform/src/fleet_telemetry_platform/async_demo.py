import asyncio

async def robot_task(name: str, delay: int):
    print(f"{name} started")

    await asyncio.sleep(delay)

    print(f"{name} finished")


async def main():
    await asyncio.gather(
        robot_task("robot 1", 2),
        robot_task("robot 2", 3),
        robot_task("robot 3", 4),
    )

asyncio.run(main())