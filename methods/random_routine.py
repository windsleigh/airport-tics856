import random
from config import checkin
import numpy as np

def random_routine(event, kind):
    match event.kind:
        # Checkin
        case "ArriveCheckIn":
            if kind == "clock":
                # time it takes for a new person to arrive to the airport
                return event.clock + np.random.gamma(3, 15, size=None)
            if kind == "checkin":
                # next checkin type
                return checkin[random.randint(1, 3)]
            if kind == "online":
                # time it takes for the person to arrive at security from the entrance
                return event.clock + np.random.gamma(3, 15, size=None)
        case "ServeCheckIn":
            if kind == "totem":
                # Time it takes for the person to pass through a totem
                return event.clock + np.random.uniform(2,3)
            if kind == "counter":
                # Time it takes for the person to pass through a counter
                return event.clock + np.random.uniform(2,3)
        case "ExitCheckIn":
            if kind == "totem":
                # time it takes for the person to arrive at security from totem
                return event.clock + np.random.gamma(3, 15, size=None)
            if kind == "counter":
                # time it takes for the person to arrive at security from counter
                return event.clock + np.random.gamma(3, 15, size=None)

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
