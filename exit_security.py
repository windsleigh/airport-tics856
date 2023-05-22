from event import Event
from main import security
from kinds import kind
from random_routine import random_routine


def exit_security(FEL, event, security_queue):
    global security

    # Check if queue is empty
    if security_queue > 0:
        queue_event = security_queue[0]

        # Gets the time spent on the queue adding the time the
        # person infront spent on the check in queue
        new_serve_clock = queue_event.clock + event.entity.time

        # Assign the same server that is free now
        queue_event.entity.server = event.entity.server

        # Schedule serve checkin event
        new_serve_event = Event(new_serve_clock, kind[5], queue_event.entity)
        FEL.append(new_serve_event)

        # Schedule arrive boarding event
        new_boarding_time = random_routine(event, "totem")
        new_boarding_event = Event(new_boarding_time, kind[7], event.entity)
        FEL.append(new_boarding_event)
        return
    else:
        # If queue is empty change server state to free
        security_queue[event.entity.server] = "free"

        # Schedule arrive boarding event
        new_boarding_time = random_routine(event, "totem")
        new_boarding_event = Event(new_boarding_time, kind[7], event.entity)
        FEL.append(new_boarding_event)
        return
