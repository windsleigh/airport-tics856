def insert_fel(FEL, event):
    for i in range(len(FEL)):
        if FEL[i].clock > event.clock:
            FEL.insert(i, event)
            return
    FEL.append(event)
