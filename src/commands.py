import asyncio
from connect import connect


async def main():
    drone = await connect()
    

    async for health in drone.telemetry.health(): 
        print(health) 
        if(health.is_global_position_ok and health.is_armable):
            print(f"Drone is ready to takeoff")
            break
    
    await drone.action.arm()
    print(f"Drone armed")
    await drone.action.set_takeoff_altitude(0.5)
    await drone.action.takeoff()
    print(f"Drone taking off")
    await asyncio.sleep(50)
    print(f"Drone is landing")
    await drone.action.land()
   

asyncio.run(main())
