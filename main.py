from boarding.arrive_boarding import arrive_boarding
from boarding.exit_boarding import exit_boarding
from boarding.serve_boarding import serve_boarding
from checkin.exit_checkin import exit_checkin
from objects.passenger import Passenger
from objects.plane import Plane
from objects.event import Event
from global_variables import *

from methods.time_routine import time_routine
from checkin.serve_checkin import serve_checkin
from checkin.arrive_checkin import arrive_checkin
from plane.arrive_plane import arrive_plane
from plane.board_plane import board_plane
from plane.exit_plane import exit_plane
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
    boarding_queue = []

    # plane = Plane(1, "arriving", None, seats - 1)
    passenger = Passenger(1, "plane", "counter", None, 0)

    passengerEvent = Event(1, "ArriveCheckIn", passenger)
    # planeEvent = Event(1, "ArrivePlane", plane)

    # FEL.append(planeEvent)
    FEL.append(passengerEvent)
    clock = 0

    for t in range(runtime):
        # evil sorting
        event, clock = time_routine(FEL, clock)
        print("main clock:", clock)
        print("event kind:", event.kind)
        print("entity:", event.entity.id)
        match event.kind:
            case "ArriveCheckIn":
                print("ArriveCheckIn ")
                arrive_checkin(FEL, event, counter_queue, totem_queue)
            case "ServeCheckIn":
                # print("ServeCheckIn")
                serve_checkin(FEL, event, clock)
            case "ExitCheckIn":
                # print("ExitCheckIn")
                exit_checkin(FEL, event, counter_queue, totem_queue)
            case "ArriveSecurity":
                # print("ArriveSecurity")
                arrive_security(FEL, event, security_queue)
            case "ServeSecurity":
                # print("ServeSecurity")
                serve_security(FEL, event)
            case "ExitSecurity":
                # print("ExitSecurity")
                exit_security(FEL, event, security_queue)
            case "ArriveBoarding":
                arrive_boarding(FEL, event)
            case "ServeBoarding":
                serve_boarding(FEL, event)
            case "ExitBoarding":
                exit_boarding(FEL, event)
            case "ArrivePlane":
                print("ArrivePlane")
                arrive_plane(FEL, event, boarding_queue)
            case "BoardPlane":
                print("BoardPlane")
                board_plane(FEL, event, boarding_queue)
            case "ExitPlane":
                print("ExitPlane")
                exit_plane(FEL, event, boarding_queue)
        print("count:", count)
        FEL.sort(key=lambda x: x.clock, reverse=True)
    print("-----End-----")


if __name__ == "__main__":
    main()
