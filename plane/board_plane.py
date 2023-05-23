from objects.event import Event
from global_variables import *
from methods.random_routine import random_routine


def board_plane(FEL, event):
    # New exit event
    next_exit_clock = random_routine(event, "leaving")
    event.entity.status = "leaving"
    new_exit_event = Event(next_exit_clock, kind[12], event.entity)
    FEL.append(new_exit_event)
    return
