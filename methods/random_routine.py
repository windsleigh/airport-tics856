import random
import numpy as np


def random_routine(event, kind):
    match event.kind:
        # Checkin
        case "ArriveCheckIn":
            if kind == "gender":
                return random.randint(0, 1)
            if kind == "clock":
                return event.clock + 2.01

            if kind == "checkin":
                checkin_types = ["counter", "totem", "online"]
                probabilities = [0.05, 0.30, 0.65]
                return np.random.choice(checkin_types, p=probabilities)
            if kind == "online":
                return event.clock + np.random.uniform(3, 4)

        case "ServeCheckIn":
            if kind == "totem":
                return event.clock + 60  # constant 60s
            if kind == "counter":
                # Log-normal distribution
                return event.clock + np.random.lognormal(
                    mean=4.18, sigma=np.sqrt(0.364)
                )

        case "ExitCheckIn":
            if kind == "totem":
                return event.clock + np.random.uniform(2, 5)
            if kind == "counter":
                return event.clock + np.random.uniform(2, 5)

        # Security
        case "ServeSecurity":
            if event.entity.gender == 0:  # male
                # Weibull distribution for males
                return event.clock + np.random.weibull(3.478) * np.sqrt(30.069)
            elif event.entity.gender == 1:  # female
                # Log-normal distribution for females
                return event.clock + np.random.lognormal(
                    mean=3.093, sigma=np.sqrt(30.069)
                )

        case "ExitSecurity":
            return event.clock + np.random.uniform(2, 5)

        # Gate
        case "ServeGate":
            # Weibull distribution
            return event.clock + np.random.weibull(2.4) * np.sqrt(18.385)

        # Plane
        case "BoardPlane":
            # Poisson distribution (15 min * 60s)
            return event.clock + 45  # np.random.poisson(lam=15 * 60)
