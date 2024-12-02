scoreboard = [[3,7]]
e1 = 0
e2 = 1
last_round = 147061000

puzzle_input = "147061"


def uusi_tilanne():
    global scoreboard, e1, e2
    
    for i in range(last_round):
        uusi_rivi = scoreboard[-1]    
        summa = int(uusi_rivi[e1]) + int(uusi_rivi[e2])
        summa_lista = list(str(summa))
        for nro in summa_lista:
            uusi_rivi.append(int(nro))
        e1_siirra = uusi_rivi[e1] + 1
        e2_siirra = uusi_rivi[e2] + 1
        e1 = (e1 + e1_siirra) % len(uusi_rivi) 
        e2 = (e2 + e2_siirra) % len(uusi_rivi) 

    return uusi_rivi

vast = uusi_tilanne()
s = ""
for c in vast:
    s += str(c)

print(s.find(puzzle_input))