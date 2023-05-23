from objects.event import Event
from global_variables import *
from methods.random_routine import random_routine


def exit_plane(FEL, event):
    global plane_queue
    if len(plane_queue) > 0:
        queue_event = plane_queue[0]
        new_serve_clock = random_routine(event, "boarding")

        # Assign the counter to the new passenger
        queue_event.entity.server = event.entity.server

        # Schedule serve boarding event for the new passenger
        new_serve_event = Event(new_serve_clock, kind[10], queue_event.entity)
        FEL.append(new_serve_event)

        # Schedule arrive boarding event for the old passenger
        event.entity.status = "arriving"
        new_arriving_time = random_routine(event, "arriving")
        new_arriving_event = Event(new_arriving_time, kind[10], event.entity)
        FEL.append(new_arriving_event)
        return

    else:
        # If queue is empty change server state to free
        plane_queue[event.entity.server] = "free"

        # Schedule arrive boarding event the old passenger
        event.entity.status = "arriving"
        new_arriving_time = random_routine(event, "arriving")
        new_arriving_event = Event(new_arriving_time, kind[10], event.entity)
        FEL.append(new_arriving_event)
        return
