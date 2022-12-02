
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

    print(sorted(summat))
    return sorted(summat)

def max_3(a):
    return a[-1] + a[-2] + a[-3]




readfile()
print(max_3(summat()))