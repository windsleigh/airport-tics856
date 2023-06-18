from config import time_in_security


def counter_security(event):
    global security_list
    init_time = event.entity.time
    exit_time = event.clock
    total_time = exit_time - init_time
    time_in_security.append(total_time)
    return
