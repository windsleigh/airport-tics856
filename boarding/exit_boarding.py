from global_variables import *
from objects.event import Event
from random_routine import random_routine


def exit_boarding(FEL, event):
    if len(gates_queues[event.entity.server]) > 0:
        queue_passenger = gates_queues[event.entity.serverserver][0]
        new_serve_clock = queue_passenger.time + event.entity.time
        queue_passenger.server = event.entity.server
        new_serve_event = Event(new_serve_clock, kind[5], queue_passenger)
        FEL.append(new_serve_event)

        # Schedule arrive boarding event
        new_exit_time = random_routine(event, "totem")
        new_boarding_event = Event(new_exit_time, kind[7], event.entity)
        FEL.append(new_boarding_event)
    else:
        # Schedule arrive boarding event
        new_exit_time = random_routine(event, "totem")
        new_boarding_event = Event(new_exit_time, kind[7], event.entity)
        FEL.append(new_boarding_event)
