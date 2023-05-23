from objects.event import Event
from methods.random_routine import random_routine
from global_variables import *


def serve_security(FEL, event):
    global security
    security[event.entity.server] = "busy"

    # Time spent on queue
    next_exit_clock = random_routine(event, "security")

    # Schedule new exit event
    new_exit_event = Event(next_exit_clock, kind[6], event.entity)
    FEL.append(new_exit_event)
    return
