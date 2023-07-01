from config import time_in_security


def counter_security(event):
    init_time = event.entity.time
    exit_time = event.clock
    total_time = exit_time - init_time
    time_in_security[exit_time] = total_time
    return
