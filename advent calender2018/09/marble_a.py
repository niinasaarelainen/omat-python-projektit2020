pelitilanteet = [[0]]
current_marble = 0
last_index = 0
players = 476
last_round = 7165700 
#last_round = 400
h = {}

def make_hash():
    for i in range(players):
        h[i] = 0

def uusi_tilanne():
    global current_marble, pelitilanteet, last_index
    
    for i in range(last_round):
        current_marble += 1
        uusi_rivi = pelitilanteet[-1]
        

        # the marble 7 marbles counter-clockwise  if %23
        if current_marble % 23 == 0:
            ind = (last_index - 7) % len(uusi_rivi) 
            nro = uusi_rivi.pop(ind)
            h[i % players] += current_marble
            h[i % players] += nro
            last_index = ind
        else:
            last_index = (last_index + 1) % len(uusi_rivi) + 1
            uusi_rivi.insert(last_index, current_marble)
            last_index = uusi_rivi.index(current_marble)



make_hash()
uusi_tilanne()
print(sorted(h.items(), key=lambda item: item[1])[-1])