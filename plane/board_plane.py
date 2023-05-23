from objects.event import Event
from global_variables import *
from methods.random_routine import random_routine


def board_plane(FEL, event):
    entrance_time = event.entity.time
    next_exit_clock = random_routine(event, "leaving")
    time_spent = next_exit_clock - entrance_time
    event.entity.time = time_spent
    event.entity.status = "leaving"
    new_exit_event = Event(next_exit_clock, kind[12], event.entity)
    FEL.append(new_exit_event)
    return
