import math
from enum import Enum

class Status(Enum):
    OK = 1
    WARN = 2
    RETURN_HOME = 3
    LAND = 4
    UNKNOWN = 5

BATTERY_WARN = 30
BATTERY_RETURN = 20
BATTERY_LAND = 10

def battery_action(percentage):
    if math.isnan(percentage):
        return Status.UNKNOWN
    elif percentage < BATTERY_LAND:
        return Status.LAND
    elif percentage < BATTERY_RETURN:
        return Status.RETURN_HOME
    elif percentage < BATTERY_WARN:
        return Status.WARN
    else:
        return Status.OK
