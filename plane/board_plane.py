from methods.insert_fel import insert_fel
from methods.random_routine import random_routine
from objects.event import Event


def board_plane(FEL, event):
    new_exit_time = random_routine(event, "exit")
    event.entity.status = "boarding"
    new_exit_event = Event(new_exit_time, "ExitPlane", event.entity)
    insert_fel(FEL, new_exit_event)

    return
