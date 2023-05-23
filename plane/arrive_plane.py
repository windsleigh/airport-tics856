from objects.event import Event
from global_variables import *
from methods.random_routine import random_routine


def arrive_plane(FEL, event):
    global board_gates
    global plane_queue
    # Set arrival time
    event.entity.time = event.clock
    # Check for free plane station
    for lane, value in enumerate(board_gates):
        if value == "free":
            # Set the station server to the passenger
            event.entity.lane = lane
            event.entity.status = "boarding"
            # Schedule next serve plan event
            new_board_event = Event(event.clock, kind[11], event.entity)
            FEL.append(new_board_event)
            return
