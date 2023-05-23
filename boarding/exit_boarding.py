from global_variables import *
from objects.event import Event
from methods.random_routine import random_routine


def exit_boarding(FEL, event):
    if len(gates_queues[event.entity.server]) > 0:
        # Get passenger in queue
        queue_passenger = gates_queues[event.entity.serverserver][0]

        # Time spent in queue
        new_serve_clock = random_routine(event, "boarding")

        # Assign the server
        queue_passenger.server = event.entity.server
        new_serve_event = Event(new_serve_clock, kind[5], queue_passenger)
        FEL.append(new_serve_event)

        # Schedule arrive boarding event
        new_exit_time = random_routine(event, "boarding")
        new_boarding_event = Event(new_exit_time, kind[7], event.entity)
        FEL.append(new_boarding_event)
    else:
        # Change server state
        gates_queues[event.entity.serverserver][0] = "free"
        # Schedule arrive boarding event
        new_exit_time = random_routine(event, "boarding")
        new_boarding_event = Event(new_exit_time, kind[7], event.entity)
        FEL.append(new_boarding_event)
