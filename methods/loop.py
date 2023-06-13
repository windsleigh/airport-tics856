from checkin.arrive_checkin import arrive_checkin
from checkin.exit_checkin import exit_checkin
from checkin.serve_checkin import serve_checkin
from gate.arrive_gate import arrive_gate
from gate.exit_gate import exit_gate
from gate.serve_gate import serve_gate
from methods.time_routine import time_routine
from objects.passenger import Passenger
from objects.plane import Plane
from objects.event import Event
from config import total_passengers_in
from config import runtime, tickets, seats, checkin_totem_list, security_list, checkin_counter_list, gate_list, total_airport_time
from plane.arrive_plane import arrive_plane
from plane.board_plane import board_plane
from plane.exit_plane import exit_plane
from security.arrive_security import arrive_security
from security.exit_security import exit_security
from security.serve_security import serve_security
import numpy as np

def print_metrics(counter_queue, totem_queue, security_queue, gate_list, total_airport_time, total_passengers_in):
    print("--- Métricas ---")
    print("Eventos:")
    print("Tiempo en check-in counter:", np.mean(checkin_counter_list))
    print("Tiempo en check-in totem:", np.mean(checkin_totem_list))
    print("Tiempo en seguridad:", np.mean(security_list))
    print("Tiempo en puerta:", np.mean(gate_list))
    print("Tiempo en aeropuerto:", np.mean(total_airport_time))
    print("Personas que pierden el avión:", np.mean(total_passengers_in))
    print("----------------")


def loop():
    # Constants
    global runtime, tickets

    # Variables
    clock = 0
    counter_queue = []
    totem_queue = []
    security_queue = []

    # Entities
    plane1 = Plane(1, "arriving", tickets - 1, seats, None, None)
    plane2 = Plane(2, "arriving", tickets, seats, None, None)
    plane3 = Plane(3, "arriving", tickets, seats, None, None)
    plane4 = Plane(4, "arriving", tickets, seats, None, None)
    plane5 = Plane(5, "arriving", tickets, seats, None, None)

    passenger = Passenger(1, plane1, "counter", None, None, None)

    # Events
    plane_event1 = Event(1, "ArrivePlane", plane1)
    plane_event2 = Event(1, "ArrivePlane", plane2)
    plane_event3 = Event(1, "ArrivePlane", plane3)
    plane_event4 = Event(1, "ArrivePlane", plane4)
    plane_event5 = Event(1, "ArrivePlane", plane5)

    passenger_event = Event(1, "ArriveCheckIn", passenger)

    # Future Event List
    FEL = [
        plane_event1,
        plane_event2,
        plane_event3,
        plane_event4,
        plane_event5,
        passenger_event,
    ]

    while runtime > 0:
        event, clock = time_routine(FEL, clock)
        match event.kind:
            # Check In routines
            case "ArriveCheckIn":
                arrive_checkin(FEL, event, counter_queue, totem_queue)
            case "ServeCheckIn":
                serve_checkin(FEL, event)
            case "ExitCheckIn":
                exit_checkin(FEL, event, counter_queue, totem_queue)

            # Security routines
            case "ArriveSecurity":
                arrive_security(FEL, event, security_queue)
            case "ServeSecurity":
                serve_security(FEL, event)
            case "ExitSecurity":
                exit_security(FEL, event, security_queue)

            # Gate routines
            case "ArriveGate":
                arrive_gate(FEL, event)
            case "ServeGate":
                serve_gate(FEL, event)
            case "ExitGate":
                exit_gate(FEL, event)

            # Plane routines
            case "ArrivePlane":
                arrive_plane(FEL, event)
            case "BoardPlane":
                board_plane(FEL, event)
            case "ExitPlane":
                exit_plane(FEL, event)
        print_metrics(counter_queue, totem_queue, security_queue, gate_list, total_airport_time, total_passengers_in)

        runtime -= 1
    print("------ Final de la simulación ------")
    print_metrics(counter_queue, totem_queue, security_queue, gate_list, total_airport_time, total_passengers_in)
