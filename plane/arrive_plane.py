from methods.insert_fel import insert_fel
from objects.event import Event
from config import gates


def arrive_plane(FEL, event):
    global gates

    try:
        free_gate = gates.index(None)
    except ValueError:
        free_gate = None

    if free_gate is not None:
        gates[free_gate] = event.entity
        event.entity.gate = free_gate
        event.entity.status = "arriving"
        new_boarding_event = Event(event.clock + 15, "BoardPlane", event.entity)
        insert_fel(FEL, new_boarding_event)
        return
