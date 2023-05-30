from config import checkin_counter_list, checkin_totem_list

def counter_checkin(event):
    global checkin_totem_list, checkin_counter_list
    if event.entity.checkin == 'totem':
        init_time = event.entity.time 
        exit_time = event.clock
        total_time = exit_time - init_time  
        checkin_totem_list.append(total_time)
    elif event.entity.checkin == 'counter':
        init_time = event.entity.time 
        exit_time = event.clock
        total_time = exit_time - init_time  
        checkin_counter_list.append(total_time)
