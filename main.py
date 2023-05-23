from checkin.exit_checkin import exit_checkin
from objects.passenger import Passenger
from objects.plane import Plane
from objects.event import Event
from global_variables import *

from methods.time_routine import time_routine
from checkin.serve_checkin import serve_checkin
from checkin.arrive_checkin import arrive_checkin
from security.arrive_security import arrive_security
from security.exit_security import exit_security
from security.serve_security import serve_security


def main():
    print("-----Start-----")
    global seats

    FEL = []
    counter_queue = []
    totem_queue = []

    security_queue = []

    # plane = Plane(1, "arriving", None, seats - 1)
    passenger = Passenger(1, "plane", "counter", None, 0)

    passengerEvent = Event(1, "ArriveCheckIn", passenger)
    # planeEvent = Event(1, "ArrivePlane", plane)

    # FEL.append(planeEvent)
    FEL.append(passengerEvent)

    for t in range(runtime):
        clock = 0
        event = time_routine(FEL, clock)
        print("main clock:", event.clock)
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
            # case "ArriveBoarding":
            #     pass
            # case "ServeBoarding":
            #     pass
            # case "ExitBoarding":
            #     pass
            # case "ArrivePlane":
            #     board_gates.append(event.entity)
            # case "BoardPlane":
            #     pass
            # case "ExitPlane":
            #     pass
    print("-----End-----")


if __name__ == "__main__":
    main()
