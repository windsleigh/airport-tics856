from event import Event
from main import security
from kinds import kind
from random_routine import random_routine


def arrive_security(FEL, event, security_queue):
    global security
    # Set arrival time
    event.entity.time = event.clock
    # Check for free security station
    for server, station in security:
        if station == "free":
            # Set the station server to the passenger
            event.entity.server = server

            # Schedule next serve security event
            new_serve_event = Event(event.clock, kind[5])
            FEL.add(new_serve_event)
    # Add to security queue if no station is empty
    security_queue.append(event)
