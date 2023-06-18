from config import gates, gate_counters, missed_flights
from methods.insert_fel import insert_fel
from objects.event import Event


def arrive_gate(FEL, event):
    global gates, gate_counters, missed_flights
    # print(gates)
    # Time passenger arrives at gate
    event.entity.time = event.clock
    # Plane is not in gate
    if gates[event.entity.plane.gate] is None:
        # Passenger missed flight
        missed_flight += 1
        # time in airport
        print(missed_flights)
        return

    # print("plane status: ", gates[event.entity.plane.gate].status)

    if gates[event.entity.plane.gate].status == "arriving":
        event.entity.plane.add_passenger(event.entity)

    if gates[event.entity.plane.gate].status == "boarding":
        # check counter state
        # If counter is free
        if gate_counters[event.entity.plane.gate] == "free":
            # New serve event
            event.entity.server = event.entity.plane.gate
            new_serve_event = Event(event.clock, "ServeGate", event.entity)
            insert_fel(FEL, new_serve_event)
            return
        else:
            # add to queue if not free
            event.entity.plane.add_passenger(event.entity)
