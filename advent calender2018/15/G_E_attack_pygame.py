import copy, pygame

data = []
e_x = 0
e_y = 0
gs = []    # [y, x]
steps_all = {}

WIDTH = 400
HEIGHT = 500


BLACK = (11, 11, 11)   
RED = (233, 3, 3)
GREEN = (3, 233, 3)
ORANGE = (190, 190, 10)

pygame.init()
font = pygame.font.SysFont("Arial", 32)
font_pieni = pygame.font.SysFont("Arial", 22)
kello = pygame.time.Clock()
naytto = pygame.display.set_mode((WIDTH, HEIGHT))


def readfile():
    # TODO   data_3-case: liiku sivulle vaikka diagonaali sanoo False 
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
        draw()
        return True

def in_range():   # ?
    for g in gs:        
        g_y = g[0]
        g_x = g[1]
        if loppuko(g_y, g_x):
            print(loppuko == "end")
            return "end"

        if data[g_y -1][g_x] == ".":
            data[g_y -1][g_x] = "?"
        if data[g_y +1][g_x] == ".":
            data[g_y +1][g_x] = "?"
        if data[g_y][g_x -1] == ".":
            data[g_y][g_x -1] = "?"
        if data[g_y][g_x +1] == ".":
            data[g_y][g_x +1] = "?"


def diagonaali1(r, m):    # reachable alafunktio, # ensin x-akseli
    print(data[r][m])
    steps = 0
    alkuloppu_x = sorted([e_x, m])
    alkuloppu_y = sorted([e_y, r])
    
    for x in range(alkuloppu_x[0] +1, alkuloppu_x[1]):          
        if data[e_y][x] != ".":
            print("@1x", data[e_y][m])  
            return False       
        steps += 1   
        #print("diag-x", steps)  
        #data[e_y][x] = "T" 
    #if ok:  
    for y in range(alkuloppu_y[0] +1, alkuloppu_y[1]):
        if data[y][m] != ".":
            print("@1y", data[y][m])  
            return False  
        steps += 1 
    key = f"{r},{m}"
    steps_all[key] = [steps + 1, "x"]
    return True

def diagonaali2(r, m):    # reachable alafunktio, # diagonaaliin ensin alas   
    print(" diag 2")
    steps = 0
    alkuloppu_x = sorted([e_x, m])
    alkuloppu_y = sorted([e_y, r])

    for y in range(alkuloppu_y[0] +1, alkuloppu_y[1]):
        if data[y][e_x] != '.':
            print("@2x", data[y][e_x])  
            return False
        steps += 1
        #data[y][e_x] = "T" 
    for x in range(alkuloppu_x[0] +1, alkuloppu_x[1]):
        if data[r][x] != ".":
            print("@2y", data[r][x])  
            return False
        steps += 1
        #data[r][x] = "T"  
     
    key = f"{r},{m}"
    if key not in steps_all:
        steps_all[key] = [steps + 1, "y"]
    return True


def reachable():   # @   
    for r in range(len(data)):
        for m in range(len(data[r])):
            if data[r][m] == "?":
                steps = 0
                ok = True

                #samalla rivillä:    
                print("r", r, "e_y", e_y)           
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
                        steps_all[key] = [steps + 1, "x"]

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
                        steps_all[key] = [steps + 1, "y"]
                 
                else:   
                    if diagonaali1(r, m) == False:  #  ensin suoraan   
                        diagonaali2(r, m)           #  ensin alas   
                    
                data[r][m] = "."  # "?" tilalle .
                
                
"""
Targets:      In range:     Reachable:    Nearest:      Chosen:
#######       #######       #######       #######       #######
#E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
#...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
#.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
#######       #######       #######       #######       #######     """

def liiku(y, x, suunta):
    global e_y, e_x

    data[e_y][e_x] = "."

    if suunta == "x":
        if x - e_x > 0:
            e_x += 1
        else:
            e_x -= 1
        
    elif suunta == "y": 
        if y - e_y > 0:
            e_y += 1
        else:
            e_y -= 1

    data[e_y][e_x] = "E"

    for g in gs:
        if loppuko(g[0], g[1]):
            return "end"

def g_t_liikkuu():
    global gs
    global e_y, e_x
    gs_copy = copy.deepcopy(gs)
    gs = []
    siirto_tehty = False

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

    draw()

    for g in gs:
        if loppuko(g[0], g[1]):
            return "end"

def draw():
    global naytto
    for r in range(len(data)):
        for s in range(len(data[r])):
            teksti = font.render(data[r][s], True, ORANGE)
            naytto.blit(teksti, (s * 40, r * 40))   
    pygame.display.flip()                                       
    kello.tick(1)  


def main():
    draw()
    i = 0

    while i < 9:
        naytto.fill(BLACK)  
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()  

        i += 1
        if in_range() == "end":
            break
        
        reachable() 
        st = [k for k, v in sorted(steps_all.items(), key=lambda item: (item[1][0], item[0]))]
        y_x = st[0].split(",")

        st2 = [v for k, v in sorted(steps_all.items(), key=lambda item: (item[1][0], item[0]))]
        suunta = st2[0][1]

        print("suunta", suunta)

        if liiku(int(y_x[0]), int(y_x[1]), suunta) == "end":
            break
        if g_t_liikkuu() == "end":
            break

        


### MAIN ###################################

readfile()
find_E_and_G() 
main()


    
    


