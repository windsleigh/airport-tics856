from global_variables import *
from objects.event import Event
from methods.random_routine import random_routine


def arrive_boarding(FEL, event):
    global board_gates

    # Get plane status
    status = "boarding"
    # event.entity.plane.status
    event.entity.time = event.clock
    # Check the passenger plane in gates
    for server, gate in enumerate(board_gates):
        if gate == event.entity.plane.id:
            if status == "arriving":
                # Add passenger to the gate queue
                gates_queues[server].append(event.entity)

            if status == "boarding":  # WIP
                if len(gates_queues[server]) > 0:
                    # Adds passenger to gate queue
                    gates_queues[server].append(event.entity)

                    # Get passenger first in line
                    queue_passenger = gates_queues[server][0]
                    new_serve_clock = random_routine(event, "boarding")

                    # Assign the server to the entity
                    queue_passenger.server = event.entity.server

                    # Schedule serve event
                    new_serve_event = Event(new_serve_clock, kind[5], queue_passenger)
                    FEL.append(new_serve_event)
                    return
                else:
                    new_serve_clock = random_routine(event, "boarding")
                    # Assign server to entity
                    queue_passenger.server = event.entity.server

                    # Schedule the new serve event
                    new_serve_event = Event(new_serve_clock, kind[5], queue_passenger)
                    FEL.append(new_serve_event)
                    return
            if status == "leaving":
                # Passenger missed the flight
                pass
