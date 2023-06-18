from methods.insert_fel import insert_fel
from metrics.gate import counter_gate
from objects.event import Event
from config import gate_counters
from metrics.total_time import total_time


def exit_gate(FEL, event):
    global gate_counters

    counter_gate(event)
    total_time(event)

    if event.entity.plane.queue_length() > 0:
        queue_passenger = event.entity.plane.get_passenger()

        queue_passenger.server = event.entity.server

        # Schedule serve gate event for the new passenger
        new_serve_event = Event(event.clock, "ServeGate", queue_passenger)
        insert_fel(FEL, new_serve_event)

        # Update plane

        if event.entity.plane.seats == 0:
            return
        else:
            event.entity.plane.board_plane()
            return

    else:
        gate_counters[event.entity.server] = "free"
        # Update Plane
        if event.entity.plane.seats == 0:
            return
        else:
            event.entity.plane.board_plane()
            return
