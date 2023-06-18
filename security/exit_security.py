from methods.insert_fel import insert_fel
from methods.random_routine import random_routine
from objects.event import Event
from config import security, security_queue
from metrics.security import counter_security


def exit_security(FEL, event):
    global security, security_queue
    counter_security(event)
    # print("Exit security event")
    # Check if queue is empty
    if len(security_queue) > 0:
        # Get first passenger from queue
        queue_passenger = security_queue.pop(0)

        # Assign the same server to the new passenger
        queue_passenger.server = event.entity.server

        # Schedule serve security event for the new passenger
        new_serve_event = Event(event.clock, "ServeSecurity", queue_passenger)
        insert_fel(FEL, new_serve_event)

        # Schedule arrive boarding event for the old passenger
        new_boarding_time = random_routine(event, "gate")
        new_boarding_event = Event(new_boarding_time, "ArriveGate", event.entity)
        insert_fel(FEL, new_boarding_event)
        return
    else:
        # If queue is empty change server state to free
        security[event.entity.server] = "free"

        # Schedule arrive boarding event for the old passenger
        new_boarding_time = random_routine(event, "gate")
        new_boarding_event = Event(new_boarding_time, "ArriveGate", event.entity)
        insert_fel(FEL, new_boarding_event)
        return
