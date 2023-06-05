from config import gate_list


def counter_gate(event):
    global gate_list
    init_time = event.entity.time
    exit_time = event.clock
    total_time = exit_time - init_time
    gate_list.append(total_time)
