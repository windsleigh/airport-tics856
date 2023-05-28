from config import security
from methods.insert_fel import insert_fel
from methods.random_routine import random_routine
from objects.event import Event


def arrive_security(FEL, event, security_queue):
    global security
    # Set arrival time
    event.entity.time = event.clock

    # Check for free security station
    for server, station in enumerate(security):
        if station == "free":
            # Set the station server to the passenger
            event.entity.server = server

            # Schedule next serve security event
            new_serve_event = Event(event.clock, "ServeSecurity", event.entity)
            insert_fel(FEL, new_serve_event)
            return
    # Add to security queue if no station is empty
    security_queue.append(event.entity)
