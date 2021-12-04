
data = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(int(rivi.strip()))

def laske_isommat():
    edellinen = data[0]
    isompi_luku_lkm = 0
    for rivi in data:
        if rivi > edellinen:
            isompi_luku_lkm += 1
        edellinen = rivi
    return isompi_luku_lkm



readfile()
print(laske_isommat())