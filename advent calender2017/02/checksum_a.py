
data = []
eroja_min = 1000


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip().split("\t"))


def checksum():
    sum = 0
    for rivi in data:
        luvut = []
        for char in rivi:
            luvut.append(int(char))
        print(max(luvut), min(luvut))
        sum += max(luvut) - min(luvut)

    return sum


readfile()
print(checksum())
 
