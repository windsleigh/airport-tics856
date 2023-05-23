from objects.event import Event
from methods.random_routine import random_routine
from global_variables import *


def serve_boarding(FEL, event):
    global gates_queues
    # Change server to busy
    gates_queues[event.entity.server] = "busy"

    # Time spent in queue
    next_exit_clock = random_routine(event, "boarding")

    # Schedule new exit event
    new_exit_event = Event(next_exit_clock, kind[9], event.entity)
    FEL.append(new_exit_event)
    return
