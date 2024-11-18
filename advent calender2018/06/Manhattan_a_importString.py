import string


data = []
max_y = 0
max_x = 0
mika_lahimpana = {}

def readfile():
    f = open("data_1.txt", "r") 
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
                print(string.ascii_uppercase[ind : ind+1], end="") 
            else:
                print(".", end="")
        print()

def piirraLopputilanne():
    for y in range(max_y +1):    # +1 muuten vika jää näkymättä, 
        for x in range(max_x + 2):   # +2 koska mallissa lopputyhjä
            if [x, y] in data:
                ind = data.index([x, y])
                print(string.ascii_uppercase[ind : ind+1], end="") 
            else:
                print(mika_lahimpana[str(x)+str(y)],  end="")
        print()


def laskeM_apu(x, y, pari):
    kohde_x = pari[0]
    kohde_y = pari[1]
    return abs(kohde_x - x) + abs(kohde_y - y)

def laskeManhattan():    
    for y in range(max_y +1):    # +1 muuten vika jää näkymättä,        
        for x in range(max_x + 2): 
            if [x, y] not in data:
                for pari in data:
                    distanssi = laskeM_apu(x, y, pari)                    
                    ind = data.index(pari)
                    if str(x)+str(y) not in mika_lahimpana:
                        mika_lahimpana[str(x)+str(y)] = [[string.ascii_lowercase[ind : ind+1], distanssi]]                  
                    else:
                        mika_lahimpana[str(x)+str(y)].append([string.ascii_lowercase[ind : ind+1], distanssi])

def tutkiHash():
    for y in range(max_y +1):    # +1 muuten vika jää näkymättä,        
        for x in range(max_x + 2): 
            if [x, y] not in data:
                etaisyydet = mika_lahimpana[str(x)+str(y)]
                print(etaisyydet)
                """ 
                s = sorted(etaisyydet, key=lambda x: x[1], reverse=True)
                if s[-1][1] == s[-2][1]:
                    mika_lahimpana[str(x)+str(y)] = "."
                else:
                    mika_lahimpana[str(x)+str(y)] = s[-1][0]  """

    

    print(list(mika_lahimpana.values()).count("."))

                    


readfile()
max_x = max([pari[0] for pari in data])
max_y = max([pari[1] for pari in data])
print(max_x, max_y)
#piirraAlkutilanne()
laskeManhattan()
print(mika_lahimpana)
#tutkiHash()
print(mika_lahimpana)
#piirraLopputilanne()