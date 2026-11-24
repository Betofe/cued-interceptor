import asyncio
from connect import connect


async def main():
    drone = await connect()
    

    async for health in drone.telemetry.health():  
        if(health.is_global_position_ok and health.is_armable):
            print(f"Drone is ready to takeoff")
            break
    
    await drone.action.arm()
    print(f"Drone armed")
    await drone.action.set_takeoff_altitude(5)
    await drone.action.takeoff()
    print(f"Drone taking off")
    await asyncio.sleep(20)
    async for position in drone.telemetry.position():
        print(position)
        latInit = position.latitude_deg
        longInit = position.longitude_deg
        absAltInit = position.absolute_altitude_m
        print(f"initial latitude: {latInit}")
        print(f"initial longitude: {longInit}")
        print(f"initial absolute altitude: {absAltInit}")
        break
    
    async for position in drone.telemetry.position():
        print(position) 
        latitude = position.latitude_deg
        longitude = position.longitude_deg
        absoluteAltitude = position.absolute_altitude_m
        print(f"latitude: {latitude}")
        print(f"longitude: {longitude}")
        print(f"absolute altitude: {absoluteAltitude}")
        break  
    latitude = latitude + 0.0002
    await drone.action.goto_location(latitude,longitude, absoluteAltitude, 0)
    await asyncio.sleep(100)
    await drone.action.goto_location(latInit, longInit, absAltInit, 0)
    await asyncio.sleep(100)
    print(f"The drone is landing")
    await drone.action.land()

asyncio.run(main())
