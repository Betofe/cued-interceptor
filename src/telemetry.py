import asyncio 
from connect import connect

async def main():

    drone = await connect()
    await asyncio.gather(read_position(drone), read_battery(drone), arm_status(drone), mode_status(drone))

async def read_position(drone):
       async for position in drone.telemetry.position():
           print(f"latitude:{position.latitude_deg}") 
           print(f"longitude: {position.longitude_deg}") 
           print(f"relative altitude: {position.relative_altitude_m}")

async def read_battery(drone):
    was_low = False;
    async for battery in drone.telemetry.battery():
        is_low = battery.remaining_percent < 30
        if (was_low != is_low):
            if(is_low):
                print(f"Battery LOW: {battery.remaining_percent}%")
              
            else:               
                print(f"Battery OK: {battery.remaining_percent}")
            was_low = is_low

async def arm_status(drone):
       last = None
       async for armed in drone.telemetry.armed():
           if(armed != last):           
             print(f"arm status: {armed}")
             last = armed

async def mode_status(drone):
       last = None
       async for mode in drone.telemetry.flight_mode():
           if(mode != last):
             print(f"flight_mode: {mode}")
             last = mode


asyncio.run(main())
  

