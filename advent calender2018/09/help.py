if current_marble % 23 == 0:
    ind = (last_index - 7) % len(uusi_rivi) 
    nro = uusi_rivi.pop(ind)
    print(nro)