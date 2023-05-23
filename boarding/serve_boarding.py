from objects.event import Event
from methods.random_routine import random_routine
from global_variables import *

def serveBoarding(FEL, event):
    global boarding_counters
    boarding_counters[event.entity.server] = "busy"
    entrance_time = event.entity.time
    next_exit_clock = random_routine(event, "boarding")
    time_spent = next_exit_clock - entrance_time
    event.entity.time = time_spent

    # Schedule new exit event
    new_exit_event = Event(next_exit_clock, kind[9], event.entity)
    FEL.append(new_exit_event)
    return