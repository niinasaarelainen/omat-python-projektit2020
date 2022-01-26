
data = []
e_x = 0
e_y = 0
gs = []    # [y, x]



def readfile():
    f = open( "data_1.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        data.append([])
        for merkki in rivi:
            data[-1].append(merkki)


def find_E_and_G():
    global e_x, e_y
    for r in range(len(data)):
        for m in range(len(data[r])):
            if data[r][m] == 'E':
                e_x = m
                e_y = r
            elif data[r][m] == 'G':
                gs.append([r, m])

def in_range():   # ?
    for g in gs:
        g_y = g[0]
        g_x = g[1]
        if data[g_y -1][g_x] == ".":
            data[g_y -1][g_x] = "?"
        if data[g_y +1][g_x] == ".":
            data[g_y +1][g_x] = "?"
        if data[g_y][g_x -1] == ".":
            data[g_y][g_x -1] = "?"
        if data[g_y][g_x +1] == ".":
            data[g_y][g_x +1] = "?"

def reachable():   # @
    for r in range(len(data)):
        for m in range(len(data[r])):
            if data[r][m] == "?":
                #samalla rivillä:
               
                ok = True
                if r == e_y:
                    for x in range(e_x +1, m):
                        if data[r][x] != ".":
                            ok = False
                            break
            if ok:        
                    data[r][m] = "@" 
                    
                            


                #samassa sarakkeessa:


                # diagonaaliin ensin suoraan

                # diagonaaliin ensin alas



"""
Targets:      In range:     Reachable:    Nearest:      Chosen:
#######       #######       #######       #######       #######
#E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
#...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
#.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
#######       #######       #######       #######       #######     """


### MAIN ###################################
readfile()


find_E_and_G() 
in_range()
for rivi in data:
    print(rivi)

reachable()
print()
for rivi in data:
    print(rivi)
