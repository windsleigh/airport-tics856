from config import gate_counters
from methods.insert_fel import insert_fel
from methods.random_routine import random_routine
from objects.event import Event


def serve_gate(FEL, event):
    print("serve gate----------------------------")
    global gate_counters

    gate_counters[event.entity.server] = "busy"

    new_exit_clock = random_routine(event, "exit")
    new_event = Event(new_exit_clock, "ExitGate", event.entity)
    insert_fel(FEL, new_event)
    return
