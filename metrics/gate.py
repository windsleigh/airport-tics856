from config import time_in_gate


def counter_gate(event):
    init_time = event.entity.time
    exit_time = event.clock
    total_time = exit_time - init_time
    time_in_gate[exit_time] = total_time
    return
