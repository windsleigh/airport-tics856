from random import *
from kinds import checkin


def random_routine(event, kind):
    match event.kind:
        case "ArriveCheckIn":
            if kind == "clock":
                # time it takes for a new person to arrive to the airport
                return event.clock + 0.05
            if kind == "checkin":
                # next checkin type
                return checkin[random.random.randint(1, 3)]
            if kind == "plane":
                pass
            if kind == "online":
                # time it takes for the person to arrive at security from the entrance
                return event.clock + 0.04
        case "ServeCheckIn":
            if kind == "totem":
                # Time it takes for the person to pass through a totem
                return event.clock + 0.05
            if kind == "counter":
                # Time it takes for the person to pass through a counter
                return event.clock + 0.08
        case "ExitCheckIn":
            if kind == "totem":
                # time it takes for the person to arrive at security from totem
                return event.clock + 0.02
            if kind == "counter":
                # time it takes for the person to arrive at security from counter
                return event.clock + 0.02
        case "ServeSecurity":
            # Time it takes for the person to pass through a security station
            return event.clock + 0.05
        case "ExitSecurity":
            # time it takes for the person to arrive at barding gate from security
            return event.clock + 0.05
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
