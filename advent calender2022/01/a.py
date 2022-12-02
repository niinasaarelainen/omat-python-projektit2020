
data = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi)

def summat():
    summat = []
    summa = 0
    for rivi in data:
        if rivi == "\n":
            summat.append(summa)
            summa = 0
        else:
            summa += int(rivi)
    summat.append(summa)

    return summat



readfile()
print(max(summat()))