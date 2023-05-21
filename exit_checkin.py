from event import Event
from random_routine import random_routine
from kinds import kind


def exit_checkin(FEL, event, counter_queue, totem_queue):
    global checkin_totems
    global checkin_counters

    # Check chekin type queue
    if event.checkin == "totem":
        # Check if totem queue is empty
        if totem_queue > 0:
            # Gets first event from the queue if its not empty
            queue_event = totem_queue[0]

            # Gets the time spent on the queue adding the time the
            # person infront spent on the check in queue
            new_serve_clock = queue_event.clock + event.entity.time

            # Assign the same server that is free now
            queue_event.entity.server = event.entity.server

            # Schedule serve checkin event
            new_serve_event = Event(new_serve_clock, kind[2], queue_event.entity)
            FEL.append(new_serve_event)

            # Schedule arrive security event
            new_security_time = random_routine(event, "totem")
            new_security_event = Event(new_security_time, kind[4], event.entity)
            FEL.append(new_security_event)
            return
        else:
            # If queue is empty change server state to free
            checkin_totems[event.entity.server] = "free"

            # Schedule new security event
            new_security_time = random_routine(event, "totem")
            new_security_event = Event(new_security_time, kind[4], event.entity)
            FEL.append(new_security_event)
            return

    if event.checkin == "counter":
        # Check if counter queue is empty
        if counter_queue > 0:
            # Gets first event from the queue if its not empty
            queue_event = totem_queue[0]

            # Gets the time spent on the queue adding the time the
            # person infront spent on the check in queue
            new_serve_clock = (
                queue_event.clock + event.entity.time
            )  # Arrival + the time the person in front took to get checked in

            # Schedule serve checkin event
            new_serve_event = Event(new_serve_clock, kind[2], queue_event.entity)
            FEL.append(new_serve_event)
            # Schedule new security event
            new_security_time = random_routine(event, "counter")
            new_security_event = Event(new_security_time, kind[4], event.entity)
            FEL.append(new_security_event)
            return
        else:
            # If queue is empty change server state to free
            checkin_counters[event.entity.server] = "free"

            # Schedule new security event
            new_security_time = random_routine(event, "counter")
            new_security_event = Event(new_security_time, kind[4], event.entity)
            FEL.append(new_security_event)
            return
