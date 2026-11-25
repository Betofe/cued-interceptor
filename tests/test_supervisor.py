import asyncio
from types import SimpleNamespace
from supervisor import supervisor_battery


class FakeAction:

    def __init__(self):
        self.return_calls = []
        self.land_calls = []

    async def return_to_launch(self):
        self.return_calls.append(1)

    async def land(self):
        self.land_calls.append(1)

class FakeTelemetry:
     
    def __init__(self, percentages):
        self.percentages = percentages

    async def battery(self):
        for value in self.percentages:

            yield SimpleNamespace(remaining_percent=value)   

class FakeDrone:

    def __init__(self, percentages):
        self.telemetry = FakeTelemetry(percentages)
        self.action = FakeAction()

def test_normal_discharge():
    drone = FakeDrone([100,25,18,5])
    asyncio.run(supervisor_battery(drone))
    assert len(drone.action.return_calls) == 1
    assert len(drone.action.land_calls) == 1


def test_flickering_reading_returns_once():
    drone = FakeDrone([100, 18, 21, 19])
    asyncio.run(supervisor_battery(drone))
    assert len(drone.action.return_calls) == 1
    assert len(drone.action.land_calls) == 0
