import copy

data = []  
sijainnit1 = []
sijainnit2 = []


def readfile():       
    f = open("data.txt", "r")         
    for rivi in f:
        merkit = []
        for merkki in rivi.strip():
            merkit.append(merkki)
        data.append(merkit)


def etsiStart():
    global start
    for rivi in range(len(data)):
        for sarake in range(len(data[0])):
            if data[rivi][sarake] == 'S':
                sijainnit2.append((rivi, sarake))
                data[rivi][sarake] = '.'


def uudetSijainnit():
    global sijainnit2, sijainnit1
    sijainnit1 = copy.deepcopy(list(set(sijainnit2)))
    #sijainnit1 = copy.deepcopy(sijainnit2)
    print(sijainnit1)
    sijainnit2 = []
    for y, x in sijainnit1:
        if y + 1 < len(data) and data[y + 1][x] == '.':
            sijainnit2.append((y + 1, x))
        if data[y - 1][x] == '.':
            sijainnit2.append((y - 1, x))
        if data[y][x + 1] == '.':
            sijainnit2.append((y, x + 1))
        if data[y][x - 1] == '.':
            sijainnit2.append((y, x - 1))

readfile()
for rivi in data:
    print(rivi)
etsiStart()

for step in range(64):
    uudetSijainnit()

print(len(set(sijainnit2)))   



