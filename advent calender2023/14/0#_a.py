data = []

def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(list(rivi.strip()))    


def piirra():
    for rivi in data:
        print(rivi)
    print()

def siirra(palloja, x, viimeisin_hash):
    for i in range(palloja):
        data[viimeisin_hash + 1 + i][x] = "O"


def tiltNorth():
    for x in range(len(data)):
        palloja = 0
        viimeisin_hash = -1
        for y in range(len(data)):
            if data[y][x] == "#":                
                siirra(palloja, x, viimeisin_hash)
                viimeisin_hash = y
                palloja = 0
            if data[y][x] == "O":
                palloja += 1
                data[y][x] = "."
        siirra(palloja, x, viimeisin_hash)


def calculateLoad():
    load = 0
    riveja = len(data)
    for y in range(len(data)):
        for x in range(len(data)):
            if data[y][x] == "O":
                load += riveja - y
    return load



readfile()
piirra()
tiltNorth()
piirra()
print(calculateLoad())