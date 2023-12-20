data = []
loads = []

def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(list(rivi.strip()))    


def piirra():
    for rivi in data:
        print(rivi)
    print()

def siirraN(palloja, x, viimeisin_hash):
    for i in range(palloja):
        data[viimeisin_hash + 1 + i][x] = "O"

def siirraS(palloja, x, viimeisin_hash):
    for i in range(palloja):
        data[viimeisin_hash - 1 - i][x] = "O"

def siirraW(palloja, y, viimeisin_hash):
    for i in range(palloja):
        data[y][viimeisin_hash + 1 + i] = "O"

def siirraE(palloja, y, viimeisin_hash):
    for i in range(palloja):
        data[y][viimeisin_hash - 1 - i] = "O"


def tiltNorth():
    for x in range(len(data)):
        palloja = 0
        viimeisin_hash = -1
        for y in range(len(data)):
            if data[y][x] == "#":                
                siirraN(palloja, x, viimeisin_hash)
                viimeisin_hash = y
                palloja = 0
            if data[y][x] == "O":
                palloja += 1
                data[y][x] = "."
        siirraN(palloja, x, viimeisin_hash)

def tiltSouth():
    for x in range(len(data)-1, -1,  -1):  # 9--> 0
        palloja = 0
        viimeisin_hash = len(data) 
        for y in range(len(data)-1, -1,  -1):
            if data[y][x] == "#":                
                siirraS(palloja, x, viimeisin_hash)
                viimeisin_hash = y
                palloja = 0
            if data[y][x] == "O":
                palloja += 1
                data[y][x] = "."
        siirraS(palloja, x, viimeisin_hash)

def tiltWest():
    for y in range(len(data)): 
        palloja = 0
        viimeisin_hash = -1
        for x in range(len(data)):
            if data[y][x] == "#":                
                siirraW(palloja, y, viimeisin_hash)
                viimeisin_hash = x
                palloja = 0
            if data[y][x] == "O":
                palloja += 1
                data[y][x] = "."
        siirraW(palloja, y, viimeisin_hash)

def tiltEast():
    for y in range(len(data)-1, -1,  -1):  # 9--> 0
        palloja = 0
        viimeisin_hash = len(data)
        for x in range(len(data)-1, -1,  -1):
            if data[y][x] == "#":                
                siirraE(palloja, y, viimeisin_hash)
                viimeisin_hash = x
                palloja = 0
            if data[y][x] == "O":
                palloja += 1
                data[y][x] = "."
        siirraE(palloja, y, viimeisin_hash)


def calculateLoad():
    load = 0
    riveja = len(data)
    for y in range(len(data)):
        for x in range(len(data)):
            if data[y][x] == "O":
                load += riveja - y
    return load

def seq_len(seq):
    guess = 1
    max_len = len(seq) // 2
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            return x, seq[0:x]

    return guess

readfile()
#piirra()
for i in range(900):
    tiltNorth() # then west,  south,  east
    #piirra()
    tiltWest() 
    #piirra()
    tiltSouth() # then west,  south,  east
    #piirra()
    tiltEast() 
    #piirra()
    loads.append((calculateLoad()))
print(loads)
print(seq_len(loads))
print(seq_len(loads[500:]))
print(loads.index(93743))

print((1000000000-136)%26)  # sekvenssin 6. alkio