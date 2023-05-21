from passenger import Passenger
from plane import Plane
from event import Event
from serve_checkin import serve_checkin
from time_routine import time_routine
from arrive_checkin import arrive_checkin

# Runtime
Runtime = 100


# Plane Capacity
seats = 100

# Gates
gates = []
last_plane = None


# Check In

checkin_counters = ["free", "free", "free", "free"]
checkin_totems = ["free", "free", "free", "free"]


def main():
    print("-----Start-----")
    global seats
    global last_plane

    FEL = []
    counter_queue = []
    totem_queue = []
    security_queue = []
    plane_queue = [False, False, False, False, False]

    plane = Plane(1, "arriving", None, seats - 1)
    passenger = Passenger(1, plane, "counter", None, 0)
    last_plane = plane.id

    passengerEvent = Event(0.1, "arrive_check_in", passenger)
    planeEvent = Event(1, "ArrivePlane", plane)

    FEL.append(passengerEvent)
    FEL.append(planeEvent)

    for minuts in range(Runtime):
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
                pass
            case "ArriveSecurity":
                pass
            case "ServeSecurity":
                pass
            case "ExitSecurity":
                pass
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
