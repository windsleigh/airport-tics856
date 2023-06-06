from methods.insert_fel import insert_fel
from objects.plane import Plane

from objects.event import Event
from config import gates, tickets
from metrics.total_passengers import passengers_in


def exit_plane(FEL, event):
    global gates
    event.entity.status = "exiting"
    passengers_in(event)
    new_plane = Plane(event.entity.id + len(gates), None, tickets, 0, None, None)

    new_exit_event = Event(event.clock, "ArrivePlane", new_plane)
    insert_fel(FEL, new_exit_event)

    gates[event.entity.gate] = None
