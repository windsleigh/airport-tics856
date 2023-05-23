from objects.event import Event
from global_variables import *
from methods.random_routine import random_routine


def exit_security(FEL, event, security_queue):
    global security

    # Check if queue is empty
    if len(security_queue) > 0:
        queue_passenger = security_queue[0]

        # time spent in queue
        new_serve_clock = random_routine(event.clock, "counter")

        # Assign the same server that is free now to the new passenger
        queue_passenger.server = event.entity.server

        # Schedule serve checkin event for the new passenger
        new_serve_event = Event(new_serve_clock, kind[5], queue_passenger)
        FEL.append(new_serve_event)

        # Schedule arrive boarding event for the old passenger
        new_boarding_time = random_routine(event, "totem")
        new_boarding_event = Event(new_boarding_time, kind[7], event.entity)
        FEL.append(new_boarding_event)
        return
    else:
        # If queue is empty change server state to free
        security[event.entity.server] = "free"

        # Schedule arrive boarding event for the old passenger
        new_boarding_time = random_routine(event, "totem")
        new_boarding_event = Event(new_boarding_time, kind[7], event.entity)
        FEL.append(new_boarding_event)
        return
