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
            return event.clock + np.random.uniform(2,3)
        case "ExitSecurity":
            # time it takes for the person to arrive at barding gate from security
            k = 0
            mean = 0.5

            # Cálculo del parámetro de escala basado en la media y el parámetro de forma
            scale = mean / k if k > 0 else np.inf

            # Generación de una muestra de la distribución Erlang utilizando la distribución gamma
            return event.clock + np.random.gamma(shape=k, scale=scale)


        # Gate
        case "ServeGate":
            return event.clock + 0.04
        # Plane
        case "BoardPlane":
            return event.clock + np.random.poisson(lam=15)