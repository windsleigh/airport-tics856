from config import security_list

def counter_security(event):
    global security_list
    init_time = event.entity.time 
    exit_time = event.clock
    total_time = exit_time - init_time  
    security_list.append(total_time)