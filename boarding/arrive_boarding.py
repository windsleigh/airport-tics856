from global_variables import *
from objects.event import Event
from random_routine import random_routine


def arrive_boarding(FEL, event, boarding_queue):
    global board_gates

    status = event.entity.plane.status
    event.entity.time = event.clock

    for server, gate in enumerate(board_gates):
        if gate == event.entity.plane.id:
            if status == "arriving":
                boarding_queue[server].append(event.entity)
            if status == "boarding":
                if len(boarding_queue[server]) > 0:
                    queue_passenger = boarding_queue[server][0]
                    new_serve_clock = queue_passenger.time + event.entity.time
                    queue_passenger.server = event.entity.server
                    new_serve_event = Event(new_serve_clock, kind[5], queue_passenger)
                    FEL.append(new_serve_event)
                    return
                else:
                    gates_queues[server][0] = "busy"
                    new_serve_clock = random_routine(event, "boarding")
                    queue_passenger.server = event.entity.server
                    new_serve_event = Event(new_serve_clock, kind[5], queue_passenger)
                    FEL.append(new_serve_event)
                    return
            if status == "leaving":
                pass
