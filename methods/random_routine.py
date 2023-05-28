import random
from config import checkin


def random_routine(event, kind):
    match event.kind:
        # Checkin
        case "ArriveCheckIn":
            if kind == "clock":
                # time it takes for a new person to arrive to the airport
                return event.clock + 0.009
            if kind == "checkin":
                # next checkin type
                return checkin[random.randint(1, 3)]
            if kind == "online":
                # time it takes for the person to arrive at security from the entrance
                return event.clock + 0.8
        case "ServeCheckIn":
            if kind == "totem":
                # Time it takes for the person to pass through a totem
                return event.clock + 0.03
            if kind == "counter":
                # Time it takes for the person to pass through a counter
                return event.clock + 0.06
        case "ExitCheckIn":
            if kind == "totem":
                # time it takes for the person to arrive at security from totem
                return event.clock + 0.04
            if kind == "counter":
                # time it takes for the person to arrive at security from counter
                return event.clock + 0.04

        # Security
        case "ServeSecurity":
            # Time it takes for the person to pass through a security station
            return event.clock + 0.1
        case "ExitSecurity":
            # time it takes for the person to arrive at barding gate from security
            return event.clock + 0.08

        # Gate
        case "ServeGate":
            return event.clock + 0.04
        # Plane
        case "BoardPlane":
            return event.clock + 2
