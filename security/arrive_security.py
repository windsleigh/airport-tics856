from objects.event import Event
from global_variables import *
from methods.random_routine import random_routine


def arrive_security(FEL, event, security_queue):
    global security
    # Set arrival time
    event.entity.time = event.clock

    # Check for free security station
    # print(event.entity.id)
    # print(event.kind)
    for server, station in enumerate(security):
        if station == "free":
            # Set the station server to the passenger
            event.entity.server = server

            # Schedule next serve security event
            new_serve_event = Event(event.clock, kind[5], event.entity)
            # print(new_serve_event.entity.id)
            # print(new_serve_event.kind)

            FEL.append(new_serve_event)
            return
    # Add to security queue if no station is empty
    security_queue.append(event.entity)
