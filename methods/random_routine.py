import random
from config import checkin
import numpy as np


# its in minutes


def random_routine(event, kind):
    match event.kind:
        # Checkin
        case "ArriveCheckIn":
            if kind == "clock":
                # time it takes for a new person to arrive to the airport
                return event.clock + np.random.gamma(5, 20, size=None)
            if kind == "checkin":
                # next checkin type
                return checkin[random.randint(1, 3)]  # fix
            if kind == "online":
                # time it takes for the person to arrive at security from the entrance
                return event.clock + 10

        case "ServeCheckIn":
            if kind == "totem":
                # Time it takes for the person to pass through a totem
                return event.clock + np.random.uniform(5, 10)
            if kind == "counter":
                # Time it takes for the person to pass through a counter
                return event.clock + np.random.uniform(10, 20)

        case "ExitCheckIn":
            if kind == "totem":
                # time it takes for the person to arrive at security from totem
                return event.clock + 10
            if kind == "counter":
                # time it takes for the person to arrive at security from counter
                return event.clock + 15

        # Security
        case "ServeSecurity":
            # Time it takes for the person to pass through a security station
            return event.clock + np.random.uniform(5, 15)

        case "ExitSecurity":
            # time it takes for the person to arrive at boarding gate from security
            k = 5
            mean = 10
            scale = mean / k if k > 0 else np.inf
            return event.clock + np.random.gamma(shape=k, scale=scale)

        # Gate
        case "ServeGate":
            return event.clock + 15
        # Plane
        case "BoardPlane":
            return event.clock + 30
