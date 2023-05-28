from methods.insert_fel import insert_fel
from objects.event import Event
from config import gate_counters


def exit_gate(FEL, event):
    print("exit_gate----------------------------")
    if event.entity.plane.queue_length() > 0:
        queue_passenger = event.entity.plane.get_passenger()

        queue_passenger.server = event.entity.server

        # Schedule serve gate event for the new passenger
        new_serve_event = Event(event.clock, "ServeGate", queue_passenger)
        insert_fel(FEL, new_serve_event)

        # Update plane

        if event.entity.plane.seats == 0:
            print("plane full missed flight")
        else:
            event.entity.plane.board_plane()
            print("yahooo----------------------------")
        return
    else:
        gate_counters[event.entity.server] = "free"
        # Update Plane
        if event.entity.plane.seats == 0:
            print("plane full missed flight")
        else:
            event.entity.plane.board_plane()
            print("yahooo----------------------------")
        return
