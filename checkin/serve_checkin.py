from objects.event import Event
from methods.random_routine import random_routine
from global_variables import *


def serve_checkin(FEL, event):
    global checkin_totems
    global checkin_counters

    # Check for chekin type
    if event.entity.checkin == "totem":
        # Changes the free server to busy
        checkin_totems[event.entity.server] = "busy"

        # Calculates the time its on checkin
        entrance_time = event.entity.time
        next_exit_clock = random_routine(event, "totem")
        time_spent = next_exit_clock - entrance_time
        event.entity.time = time_spent

        # Schedule new exit event
        new_exit_event = Event(next_exit_clock, kind[3], event.entity)
        FEL.append(new_exit_event)

        return
    if event.entity.checkin == "counter":
        # Changes the free server to busy
        checkin_counters[event.entity.server] = "busy"

        # Calculates the time its on checkin
        entrance_time = event.entity.time
        next_exit_clock = random_routine(event, "counter")
        time_spent = next_exit_clock - entrance_time
        event.entity.time = time_spent

        # Schedule new exit event
        new_exit_event = Event(next_exit_clock, kind[3], event.entity)
        FEL.append(new_exit_event)
        return
