from config import checkin_counters, checkin_totems, counter_queue, totem_queue
from methods.insert_fel import insert_fel
from methods.random_routine import random_routine
from objects.event import Event
from metrics.checkin import counter_checkin


def exit_checkin(FEL, event):
    global checkin_totems, checkin_counters, counter_queue, totem_queue
    counter_checkin(event)

    # Check chekin type queue
    if event.entity.checkin == "totem":
        # Check if totem queue is empty

        if len(totem_queue) > 0:
            # Gets first event from the queue if its not empty
            queue_passenger = totem_queue.pop(0)

            # Assign the same server that is free now
            queue_passenger.server = event.entity.server

            # Schedule serve checkin event
            new_serve_event = Event(event.clock, "ServeCheckIn", queue_passenger)
            insert_fel(FEL, new_serve_event)

            # Schedule arrive security event
            new_security_time = random_routine(event, "totem")
            new_security_event = Event(
                new_security_time, "ArriveSecurity", event.entity
            )

            insert_fel(FEL, new_security_event)
            return
        else:
            # If queue is empty change server state to free
            checkin_totems[event.entity.server] = "free"

            # Schedule new security event
            new_security_time = random_routine(event, "totem")
            new_security_event = Event(
                new_security_time, "ArriveSecurity", event.entity
            )
            insert_fel(FEL, new_security_event)
            return

    if event.entity.checkin == "counter":
        # Check if counter queue is empty
        if len(counter_queue) > 0:
            # Gets first event from the queue if its not empty
            queue_passenger = counter_queue.pop(0)

            # Assign the same server that is free now
            queue_passenger.server = event.entity.server

            # Schedule serve checkin event
            new_serve_event = Event(event.clock, "ServeCheckIn", queue_passenger)
            insert_fel(FEL, new_serve_event)

            # Schedule new security event
            new_security_time = random_routine(event, "counter")
            new_security_event = Event(
                new_security_time, "ArriveSecurity", event.entity
            )
            insert_fel(FEL, new_security_event)
            return
        else:
            # If queue is empty change server state to free
            checkin_counters[event.entity.server] = "free"

            # Schedule new security event
            new_security_time = random_routine(event, "counter")
            new_security_event = Event(
                new_security_time, "ArriveSecurity", event.entity
            )
            insert_fel(FEL, new_security_event)
            return
