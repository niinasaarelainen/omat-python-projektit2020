
data = []
total = 0


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(int(rivi.strip()))


def laske():
    global total

    for rivi in data:
        while rivi > 6:
            tulos = rivi // 3 - 2
            total += tulos
            rivi = tulos
            print(total)
   
    return total



readfile()
print(laske())
