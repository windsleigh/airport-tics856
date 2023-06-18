from config import checkin_counters, checkin_totems
from methods.insert_fel import insert_fel
from methods.random_routine import random_routine
from objects.event import Event


def serve_checkin(FEL, event):
    global checkin_totems
    global checkin_counters
    # print("Serve checkin event")
    # Check for chekin type
    if event.entity.checkin == "totem":
        # Changes the free server to busy
        checkin_totems[event.entity.server] = "busy"

        # Calculates the time on queue
        next_exit_clock = random_routine(event, "totem")

        # Schedule new exit event
        new_exit_event = Event(next_exit_clock, "ExitCheckIn", event.entity)
        insert_fel(FEL, new_exit_event)
        return

    if event.entity.checkin == "counter":
        # Changes the free server to busy
        checkin_counters[event.entity.server] = "busy"

        # Calculates the time on queue
        next_exit_clock = random_routine(event, "counter")

        # Schedule new exit event
        new_exit_event = Event(next_exit_clock, "ExitCheckIn", event.entity)
        insert_fel(FEL, new_exit_event)
        return
