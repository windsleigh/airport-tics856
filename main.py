from exit_security import exit_security
from passenger import Passenger
from plane import Plane
from event import Event
from serve_security import serve_security
from time_routine import time_routine

from arrive_checkin import arrive_checkin
from serve_checkin import serve_checkin
from exit_checkin import exit_checkin

from arrive_security import arrive_security

# Runtime
runtime = 100


# Plane Capacity
seats = 100

# Gates
gates = 5
board_gates = [] * gates
last_plane = None

# Check In
counters = 5
checkin_counters = ["free"] * counters
totems = 5
checkin_totems = ["free"] * totems

# Security
stations = 5
security = ["free"] * stations


def main():
    print("-----Start-----")
    global seats
    global last_plane

    FEL = []
    counter_queue = []
    totem_queue = []
    security_queue = []
    total_planes_queue = 5
    plane_queue = [False] * total_planes_queue

    plane = Plane(1, "arriving", None, seats - 1)
    passenger = Passenger(1, plane, "counter", None, 0)
    last_plane = plane.id

    passengerEvent = Event(0.1, "arrive_check_in", passenger)
    planeEvent = Event(1, "ArrivePlane", plane)

    FEL.append(passengerEvent)
    FEL.append(planeEvent)

    for t in range(runtime):
        clock = 0
        event = time_routine(FEL, clock)
        match event.kind:
            case "ArriveCheckIn":
                print("ArriveCheckIn")
                arrive_checkin(FEL, event, counter_queue, totem_queue)
            case "ServeCheckIn":
                print("ServeCheckIn")
                serve_checkin(FEL, event)
            case "ExitCheckIn":
                print("ExitCheckIn")
                exit_checkin(FEL, event, counter_queue, totem_queue)
            case "ArriveSecurity":
                print("ArriveSecurity")
                arrive_security(FEL, event, security_queue)
            case "ServeSecurity":
                print("ServeSecurity")
                serve_security(FEL, event)
            case "ExitSecurity":
                print("ExitSecurity")
                exit_security(FEL, event, security_queue)
            case "ArriveBoarding":
                pass
            case "ServeBoarding":
                pass
            case "ExitBoarding":
                pass
            case "ArrivePlane":
                pass
            case "BoardPlane":
                pass
            case "ExitPlane":
                pass

    print("-----End-----")


if __name__ == "__main__":
    main()
