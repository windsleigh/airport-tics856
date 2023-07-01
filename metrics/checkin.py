from config import time_in_totems, time_in_counters


def counter_checkin(event):
    if event.entity.checkin == "totem":
        init_time = event.entity.time
        exit_time = event.clock
        total_time = exit_time - init_time
        time_in_totems[exit_time] = total_time
        return

    elif event.entity.checkin == "counter":
        init_time = event.entity.time
        exit_time = event.clock
        total_time = exit_time - init_time
        time_in_counters[exit_time] = total_time
        return
