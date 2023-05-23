from objects.event import Event
from methods.random_routine import random_routine
from global_variables import *


def serve_security(FEL, event):
    global security
    security[event.entity.server] = "busy"

    # Calculates the time its on checkin
    entrance_time = event.entity.time
    next_exit_clock = random_routine(event, "totem")
    time_spent = next_exit_clock - entrance_time
    event.entity.time = time_spent

    # Schedule new exit event
    new_exit_event = Event(next_exit_clock, kind[6], event.entity)
    FEL.append(new_exit_event)
    return
