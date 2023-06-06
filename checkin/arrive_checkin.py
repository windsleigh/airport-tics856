from methods.insert_fel import insert_fel
from methods.random_plane import random_plane
from methods.random_routine import random_routine
from objects.passenger import Passenger
from objects.event import Event
from config import checkin_counters, checkin_totems



def arrive_checkin(FEL, event, counter_queue, totem_queue):
    global checkin_counters, checkin_totems

    # Checkin arrival time
    event.entity.time = event.clock
    event.entity.arrival_time = event.clock
    # Next airport arrival
    new_arrival_plane = random_plane()
    new_arrival_clock = random_routine(event, "clock")
    new_arrival_checkin = random_routine(event, "checkin")
    new_arrival_passenger = Passenger(
        event.entity.id + 1, new_arrival_plane, new_arrival_checkin, None, None, None
    )

    # Schedule next arrival
    new_arrival_event = Event(new_arrival_clock, "ArriveCheckIn", new_arrival_passenger)

    # Insert event in FEL
    insert_fel(FEL, new_arrival_event)

    # Check checkin type
    if event.entity.checkin == "online":
        # Schedule arrive security event
        new_security_time = random_routine(event, "online")
        new_security_event = Event(new_security_time, "ArriveSecurity", event.entity)
        insert_fel(FEL, new_security_event)
        return

    elif event.entity.checkin == "totem":
        # Check for free totems
        for server, totem in enumerate(checkin_totems):
            if totem == "free":
                # Set the totem server to the passenger
                event.entity.server = server

                # Schedule next serve event
                new_totem_event = Event(event.clock, "ServeCheckIn", event.entity)
                insert_fel(FEL, new_totem_event)
                return
        # If no totem is free add it to the counter queue
        totem_queue.append(event.entity)
        return

    elif event.entity.checkin == "counter":
        # Check for free counters
        for server, counter in enumerate(checkin_counters):
            if counter == "free":
                # Set the counter server to the passenger
                event.entity.server = server

                # Schedule next serve event
                new_counter_event = Event(event.clock, "ServeCheckIn", event.entity)
                insert_fel(FEL, new_counter_event)
                return
        # If no counter is free add it to the counter queue
        counter_queue.append(event.entity)
        return
