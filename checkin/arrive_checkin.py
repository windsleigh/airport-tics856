from objects.passenger import Passenger
from objects.event import Event
from methods.random_routine import random_routine
from global_variables import *

# from methods.get_plane import get_plane


# import methods.get_plane as get_plane
from global_variables import *


def arrive_checkin(FEL, event, counter_queue, totem_queue):
    global checkin_counters
    global checkin_totems

    # Save chekin arrival time
    event.entity.time = event.clock

    # Next airport arrival event
    next_clock = random_routine(event, "clock")
    # print("next clock:", next_clock)
    next_checkin_type = random_routine(event, "checkin")
    next_passenger = Passenger(
        event.entity.id + 1, "get_plane()", next_checkin_type, None, 0
    )
    next_arrive_event = Event(next_clock, kind[1], next_passenger)
    FEL.append(next_arrive_event)

    # Check checkin type
    if event.entity.checkin == "online":
        # Schedule arrive security event
        new_security_time = random_routine(event, "online")
        new_security_event = Event(new_security_time, kind[4], next_passenger)
        FEL.append(new_security_event)
        return

    elif event.entity.checkin == "totem":
        # Check for free totems
        for server, totem in enumerate(checkin_totems):
            if totem == "free":
                # Set the totem server to the passenger
                event.entity.server = server

                # Schedule next serve event

                next_totem_event = Event(event.clock + 1, kind[2], event.entity)
                FEL.append(next_totem_event)
                return
        # If no totem is free add it to the counter queue
        totem_queue.append(event)
        return

    elif event.entity.checkin == "counter":
        # Check for free counters
        for server, counter in enumerate(checkin_counters):
            if counter == "free":
                # Set the counter server to the passenger
                event.entity.server = server

                # Schedule next serve event
                next_counter_event = Event(event.clock + 1, kind[2], event.entity)
                FEL.append(next_counter_event)
                return
        # If no counter is free add it to the counter queue
        counter_queue.append(event)
        return
