import copy

data = []
wide = 50    
tall =6
kuva = []

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip().split(" "))

def luoKuva():
    for y in range(tall):
        rivi = []
        for x in range(wide):
            rivi.append(".")
        kuva.append(rivi)

def printtaaKuva(ohje):
    print("\n", ohje)
    for rivi in kuva:
        for chr in rivi:
            print(chr, end = '')
        print()

def modify():
    global kuva
    for rivi in data:
        if 'rect' in rivi:
            x_montako = int(rivi[1].split('x')[0])        # rect 3x2 
            y_montako = int(rivi[1].split('x')[1])
            for y in range(y_montako):
                for x in range(x_montako):
                    kuva[y][x] = "#"

        if 'rotate' in rivi:
            if 'column' in rivi:    # rotate column x=1 by 1 
                x = int(rivi[2][2])
                amount = int(rivi[-1])
                bu = copy.deepcopy(kuva)
                for y in range(tall):
                    y_uusi = (y + amount ) % tall
                    bu[y_uusi][x] = kuva[y][x]
                kuva = copy.deepcopy(bu)
            if 'row' in rivi:       # rotate row y=0 by 10
                y = int(rivi[2][2])
                amount = int(rivi[-1])
                bu = copy.deepcopy(kuva)
                for x in range(wide):
                    x_uusi = (x + amount ) % wide
                    bu[y][x_uusi] = kuva[y][x]
                kuva = copy.deepcopy(bu)
        printtaaKuva(rivi)

def laskeValot():
    valoja = 0
    for rivi in kuva:
        valoja += rivi.count("#")
    return valoja



readfile()
luoKuva()
modify()
print(laskeValot())   # 100 too low
