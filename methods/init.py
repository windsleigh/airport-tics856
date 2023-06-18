from objects.passenger import Passenger
from objects.plane import Plane
from objects.event import Event
from config import runtime, tickets, seats


def init_routine(FEL, clock):
    clock = 0
    plane1 = Plane(1, "arriving", tickets - 1, seats, None, None)
    plane2 = Plane(2, "arriving", tickets, seats, None, None)
    plane3 = Plane(3, "arriving", tickets, seats, None, None)
    plane4 = Plane(4, "arriving", tickets, seats, None, None)
    plane5 = Plane(5, "arriving", tickets, seats, None, None)

    passenger = Passenger(1, plane1, "counter", None, None)

    init_events = [
        Event(1, "ArrivePlane", plane1),
        Event(1, "ArrivePlane", plane2),
        Event(1, "ArrivePlane", plane3),
        Event(1, "ArrivePlane", plane4),
        Event(1, "ArrivePlane", plane5),
        Event(1, "ArriveCheckIn", passenger),
    ]
    FEL.append(init_events)
    statical_counters = [0, 0, 0, 0, 0]
    return
