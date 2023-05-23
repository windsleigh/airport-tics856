import random

# from get_plane import get_plane
from global_variables import checkin


def random_routine(event, kind):
    match event.kind:
        case "ArriveCheckIn":
            if kind == "clock":
                # time it takes for a new person to arrive to the airport
                return event.clock + 1
            if kind == "checkin":
                # next checkin type
                return checkin[random.randint(1, 3)]
            if kind == "plane":
                return "get_plane()"
            if kind == "online":
                # time it takes for the person to arrive at security from the entrance
                return event.clock + 4

        case "ServeCheckIn":
            if kind == "totem":
                # Time it takes for the person to pass through a totem
                return event.clock + 4
            if kind == "counter":
                # Time it takes for the person to pass through a counter
                return event.clock + 4

        case "ExitCheckIn":
            if kind == "totem":
                # time it takes for the person to arrive at security from totem
                return event.clock + 4
            if kind == "counter":
                # time it takes for the person to arrive at security from counter
                return event.clock + 4

        case "ServeSecurity":
            # Time it takes for the person to pass through a security station
            return event.clock + 4

        case "ExitSecurity":
            # time it takes for the person to arrive at barding gate from security
            return event.clock + 4

        case "ArriveBoarding":
            return event.clock + 4
        case "ServeBoarding":
            return event.clock + 4
        case "ExitBoarding":
            return event.clock + 4
        case "ArrivePlane":
            return event.clock + 4
        case "BoardPlane":
            return event.clock + 4
        case "ExitPlane":
            return event.clock + 4
