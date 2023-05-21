from event import Event
from random_routine import random_routine
from kinds import kind


def serve_checkin(FEL, event):
    global checkin_totems
    global checkin_counters

    if event.checkin == "totem":
        checkin_totems[event.entity.server] = "busy"
        entrance_time = event.time
        next_exit_clock = random_routine(event, "totem")

        time_spent = next_exit_clock - entrance_time
        event.entity.time = time_spent
        new_exit_event = Event(next_exit_clock, kind[3], event.entity)
        FEL.append(new_exit_event)
        return
    if event.checkin == "counter":
        checkin_counters[event.entity.server] = "busy"

        next_exit_clock = random_routine(event, "counter")
        new_exit_event = Event(next_exit_clock, kind[3], event.entity)
        FEL.append(new_exit_event)
        return
