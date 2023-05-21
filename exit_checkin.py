from event import Event
from random_routine import random_routine
from kinds import kind


def exit_checkin(FEL, event, counter_queue, totem_queue):
    global checkin_totems
    global checkin_counters

    if event.checkin == "totem":
        if totem_queue > 0:
            queue_event = totem_queue[0]
            new_serve_clock = queue_event.clock + event.entity.time
            queue_event.entity.server = event.entity.server
            new_serve_event = Event(new_serve_clock, kind[2], queue_event.entity)
            FEL.append(new_serve_event)

            new_security_time = random_routine(event, "totem")
            new_security_event = Event(new_security_time, kind[4], event.entity)
            FEL.append(new_security_event)
            return
        else:
            checkin_totems[event.entity.server] = "free"

            new_security_time = random_routine(event, "totem")
            new_security_event = Event(new_security_time, kind[4], event.entity)
            FEL.append(new_security_event)
            return

    if event.checkin == "counter":
        if counter_queue > 0:
            queue_event = totem_queue[0]
            new_serve_clock = queue_event.clock + event.entity.time
            new_serve_event = Event(new_serve_clock, kind[2], queue_event.entity)
            FEL.append(new_serve_event)

            new_security_time = random_routine(event, "counter")
            new_security_event = Event(new_security_time, kind[4], event.entity)
            FEL.append(new_security_event)
            return
        else:
            checkin_counters[event.entity.server] = "free"

            new_security_time = random_routine(event, "counter")
            new_security_event = Event(new_security_time, kind[4], event.entity)
            FEL.append(new_security_event)
            return
