import asyncio 
from mavsdk import System

async def connect(address="udpin://0.0.0.0:14551"):
    drone = System()

    await drone.connect(system_address=address)

    async for state in drone.core.connection_state():

        if state.is_connected:
            print("Connected")
            return drone
async def main():
    await connect()

if __name__ == "__main__":
    asyncio.run(main())
