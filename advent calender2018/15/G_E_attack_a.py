
data = []
e_x = 0
e_y = 0
gs = []    # [y, x]
steps_all = {}



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
                        data[r][m] = "@" 
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
                        data[r][m] = "@" 
                        key = f"{r},{m}"
                        steps_all[key] = steps + 1

                # diagonaaliin ensin suoraan     
                else:
                    alkuloppu_x = sorted([e_x, m])
                    alkuloppu_y = sorted([e_y, r])
                    for x in range(alkuloppu_x[0] +1, alkuloppu_x[1] + 1):
                        print("r", r, "x", x)
                        if data[e_y][x] != ".":
                            ok = False
                            break
                        else:
                            steps += 1
                            print("step+1 x")
                            data[e_y][x] = "T" 
                    if ok:      
                        for y in range(alkuloppu_y[0] +1, alkuloppu_y[1]):
                            if data[y][m] != ".":
                                ok = False
                                break   
                            else:
                                steps += 1
                                print("step+1 y")
                                data[y][m] = "T" 
                    if ok:        
                        data[r][m] = "@" 
                        key = f"{r},{m}"
                        steps_all[key] = steps + 1
                        print(steps + 1)

                # diagonaaliin ensin alas   # TODO piirrä reitti testimielessä !!!!!!!
                    for y in range(alkuloppu_y[0] +1, alkuloppu_y[1] + 1):
                        if data[y][m] != ".":
                            ok = False
                            break   
                        else:
                            steps += 1
                            print("step+1 y")
                            data[y][m] = "T" 
                    if ok:
                        for x in range(alkuloppu_x[0] +1, alkuloppu_x[1]):
                            if data[e_y][x] != ".":
                                ok = False
                                break
                            else:
                                steps += 1
                                print("step+1 x")
                                data[e_y][x] = "T"  
                    if ok:        
                        data[r][m] = "@" 
                        key = f"{r},{m}"
                        steps_all[key] = steps + 1
                        print(steps + 1)



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

print(steps_all)