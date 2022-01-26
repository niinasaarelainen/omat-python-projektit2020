import copy

data = []
e_x = 0
e_y = 0
gs = []    # [y, x]
steps_all = {}



def readfile():
    f = open( "data_3.txt", "r") 
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


def loppuko(y, x):
    if 'G' in [data[e_y -1][e_x], data[e_y +1][e_x], data[e_y][e_x -1], data[e_y][e_x +1]]:
        print("   END")
        return True

def in_range():   # ?
    for g in gs:        
        g_y = g[0]
        g_x = g[1]
        if loppuko(g_y, g_x):
            return "end"

        if data[g_y -1][g_x] == ".":
            data[g_y -1][g_x] = "?"
        if data[g_y +1][g_x] == ".":
            data[g_y +1][g_x] = "?"
        if data[g_y][g_x -1] == ".":
            data[g_y][g_x -1] = "?"
        if data[g_y][g_x +1] == ".":
            data[g_y][g_x +1] = "?"


def diagonaalit(r, m):    # reachable alafunktio
    steps = 0
    ok = True
    alkuloppu_x = sorted([e_x, m])
    alkuloppu_y = sorted([e_y, r])
    for x in range(alkuloppu_x[0] +1, alkuloppu_x[1] + 1):
        if data[e_y][x] != ".":
            ok = False
            break
        else:
            steps += 1
            #data[e_y][x] = "T" 
    if ok:      
        for y in range(alkuloppu_y[0] +1, alkuloppu_y[1]):
            if data[y][m] != ".":
                ok = False
                break   
            else:
                steps += 1
                #data[y][m] = "T" 
    if ok:      
        key = f"{r},{m}"
        steps_all[key] = steps + 1
        print(steps + 1)

# diagonaaliin ensin alas   
    ok = True
    steps = 0
    for y in range(alkuloppu_y[0] +1, alkuloppu_y[1] + 1):
        if data[y][e_x] != ".":
            ok = False
            break   
        else:
            steps += 1
            #data[y][e_x] = "T" 
    if ok:
        for x in range(alkuloppu_x[0] +1, alkuloppu_x[1]):
            if data[r][x] != ".":
                ok = False
                break
            else:
                steps += 1
                #data[r][x] = "T"  
    if ok:   
        key = f"{r},{m}"
        if key not in steps_all:
            steps_all[key] = steps + 1
        print(steps + 1)


def reachable():   # @   
    for r in range(len(data)):
        for m in range(len(data[r])):
            if data[r][m] == "?":
                steps = 0
                #samalla rivillä:
                ok = True
                if r == e_y:
                    alkuloppu = sorted([e_x, m])
                    for x in range(alkuloppu[0] +1, alkuloppu[1]):                        
                        if data[r][x] != ".":
                            ok = False
                            break
                        else:
                            steps += 1
                    if ok:  
                        key = f"{r},{m}"
                        steps_all[key] = steps + 1

                #samassa sarakkeessa:
                elif m == e_x:
                    alkuloppu = sorted([e_y, r])
                    for y in range(alkuloppu[0] +1, alkuloppu[1]):                        
                        if data[y][e_x] != ".":                            
                            ok = False
                            break
                        else:
                            steps += 1
                    if ok:        
                        key = f"{r},{m}"
                        steps_all[key] = steps + 1

                # diagonaaliin ensin suoraan     
                else:
                    diagonaalit(r, m)
                    
                data[r][m] = "."
            



"""
Targets:      In range:     Reachable:    Nearest:      Chosen:
#######       #######       #######       #######       #######
#E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
#...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
#.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
#######       #######       #######       #######       #######     """

def liiku(y, x):
    global e_y, e_x
    data[e_y][e_x] = "."
    if x == e_x:
        if y - e_y > 0:
            e_y += 1
        else:
            e_y -= 1
    else:
        if x - e_x > 0:
            e_x += 1
        else:
            e_x -= 1
    data[e_y][e_x] = "E"

    print()
    for rivi in data:
        print(rivi)

    for g in gs:
        if loppuko(g[0], g[1]):
            return "end"

def g_t_liikkuu():
    global gs
    global e_y, e_x
    gs_copy = copy.deepcopy(gs)
    gs = []
    siirto_tehty = False

    print("len(gs_copy)", len(gs_copy))
    for g in gs_copy:
        siirto_tehty = False
        data[g[0]][g[1]] = "."
        if g[1] == e_x:
            if g[0] - e_y > 0 and data[g[0] - 1][g[1]] == ".":
                data[g[0] - 1][g[1]] = "G"
                gs.append([g[0] - 1, g[1]])
                siirto_tehty = True
            elif g[0] - e_y < 0 and data[g[0] + 1][g[1]] == ".":
                data[g[0] + 1][g[1]] = "G"
                gs.append([g[0] + 1, g[1]])
                siirto_tehty = True
        if siirto_tehty == False:
            #print("siirto_tehty == False")
            if g[1] - e_x > 0 and data[g[0]][g[1] -1] == ".":
                data[g[0]][g[1] -1] = "G"
                gs.append([g[0], g[1] - 1])
                siirto_tehty = True
            elif g[1] - e_x < 0 and data[g[0]][g[1] +1] == ".":
                data[g[0]][g[1] +1] = "G"
                gs.append([g[0], g[1] + 1])
                siirto_tehty = True
        if siirto_tehty == False:
            if g[0] - e_y > 0 and data[g[0] - 1][g[1]] == ".":
                data[g[0] - 1][g[1]] = "G"
                gs.append([g[0] - 1, g[1]])   
                siirto_tehty = True             
            elif g[0] - e_y < 0 and data[g[0] + 1][g[1]] == ".":
                data[g[0] + 1][g[1]] = "G"
                gs.append([g[0] + 1, g[1]]) 
                siirto_tehty = True
        if siirto_tehty == False:
            data[g[0]][g[1]] = "G" 

    print()
    for rivi in data:
        print(rivi)

    for g in gs:
        if loppuko(g[0], g[1]):
            return "end"
        
    

### MAIN ###################################

readfile()
find_E_and_G() 

#while True:
for i in range(3):     
    if in_range() == "end":
        break
    
    reachable()
    
    print(steps_all)
    st = [k for k, v in sorted(steps_all.items(), key=lambda item: (item[1], item[0]))]
    y_x = st[0].split(",")
    print(y_x)

    if liiku(int(y_x[0]), int(y_x[1])) == "end":
        break
    if g_t_liikkuu() == "end":
        break
    
    


