from methods.insert_fel import insert_fel
from objects.plane import Plane

from objects.event import Event
from config import gates, tickets, plane_history


def exit_plane(FEL, event):
    global gates, plane_history
    event.entity.status = "exiting"

    plane_history[event.entity.id] = {
        "status": "exited",
        "exit_time": event.clock,
        "gate": event.entity.gate,
        # add more information about the plane here if needed
    }

    new_plane = Plane(event.entity.id + len(gates), None, tickets, 0, None, None)
    new_exit_event = Event(event.clock, "ArrivePlane", new_plane)
    insert_fel(FEL, new_exit_event)

    gates[event.entity.gate] = None
    return
