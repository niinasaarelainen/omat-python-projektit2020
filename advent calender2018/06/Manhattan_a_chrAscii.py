
data = []
max_y = 0
max_x = 0
mika_lahimpana = {}
reunoissa = []
potentiaaliset_vastaukset = []

def readfile():
    f = open("data_test2.txt", "r") 
    for rivi in f:
        x, y = rivi.split(", ")
        x = int(x)
        y = int(y)
        data.append([x, y])

 

def piirraAlkutilanne():
    for y in range(max_y +1):    # +1 muuten vika jää näkymättä, 
        for x in range(max_x + 2):   # +2 koska mallissa lopputyhjä
            if [x, y] in data:
                ind = data.index([x, y])
                print(chr(97 + ind), end="") 
            else:
                print(".", end="")
        print()

def piirraLopputilanne():
    for y in range(max_y +1):    # +1 muuten vika jää näkymättä, 
        for x in range(max_x + 2):   # +2 koska mallissa lopputyhjä
            
            if x == 0 or y == 0 or x == max_x or y == max_y:
                reunoissa.append(mika_lahimpana[str(x)+str(y)][0])           
            else:
                print(mika_lahimpana[str(x)+str(y)],  end="")
    print("reunoissa", reunoissa)
    print("mika_lahimpana", mika_lahimpana)


def laskeM_apu(x, y, pari):
    kohde_x = pari[0]
    kohde_y = pari[1]
    return abs(kohde_x - x) + abs(kohde_y - y)

def laskeManhattan():    
    for y in range(max_y +1):    # +1 muuten vika jää näkymättä,        
        for x in range(max_x + 2): 
            
            for pari in data:
                distanssi = laskeM_apu(x, y, pari)                    
                ind = data.index(pari)
                if str(x)+str(y) not in mika_lahimpana:
                    mika_lahimpana[str(x)+str(y)] = [[chr(65 + ind), distanssi]]                  
                else:
                    mika_lahimpana[str(x)+str(y)].append([chr(65 + ind), distanssi])

def tutkiHash():
    for y in range(max_y +1):    # +1 muuten vika jää näkymättä,        
        for x in range(max_x + 2): 
            if [x, y] not in data:
                etaisyydet = mika_lahimpana[str(x)+str(y)]
                print(etaisyydet)
                s = sorted(etaisyydet, key=lambda x: x[1], reverse=True)
                if s[-1][1] == s[-2][1]:
                    mika_lahimpana[str(x)+str(y)] = "."
                else:
                    mika_lahimpana[str(x)+str(y)] = s[-1][0]     

def vastaus():
    max = 0
    for k, v in mika_lahimpana.items():
        if v not in reunoissa:
            if list(mika_lahimpana.values()).count(v) + 1 > max:
                max = list(mika_lahimpana.values()).count(v) + 1
                print("  v", v)
    print(max)        


readfile()
max_x = max([pari[0] for pari in data])
max_y = max([pari[1] for pari in data])
print(max_x, max_y)
#piirraAlkutilanne()
laskeManhattan()
tutkiHash()
piirraLopputilanne()
vastaus()
