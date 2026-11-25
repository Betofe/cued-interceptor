from health import battery_action, Status

SEVERITY = {
    Status.OK: 0,
    Status.UNKNOWN: 0,
    Status.WARN: 0,
    Status.RETURN_HOME: 1,
    Status.LAND: 2,
}

async def supervisor_battery(drone):
    last_action = None
    highest = 0
    
    async for battery in drone.telemetry.battery():
        action = battery_action(battery.remaining_percent)
        if SEVERITY[action] < highest:
            continue
        if(action != last_action):
            if (action == Status.OK):
                print(f"battery is fine")


            elif (action == Status.WARN):
                print(f"battery failsafe: {battery.remaining_percent}%")

   
            elif (action == Status.RETURN_HOME):
                print(f"returning home position")
                await drone.action.return_to_launch()


            elif (action == Status.LAND):
                print(f"landing")
                await drone.action.land()


            elif (action == Status.UNKNOWN):
                print(f"battery reading unavailable")

            
            last_action = action
            highest = max(highest, SEVERITY[action])

