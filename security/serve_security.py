from methods.insert_fel import insert_fel
from methods.random_routine import random_routine
from objects.event import Event
from config import security


def serve_security(FEL, event):
    global security
    security[event.entity.server] = "busy"

    # Time spent on queue
    next_exit_clock = random_routine(event, "security")

    # Schedule new exit event
    new_exit_event = Event(next_exit_clock, "ExitSecurity", event.entity)
    insert_fel(FEL, new_exit_event)
    return
