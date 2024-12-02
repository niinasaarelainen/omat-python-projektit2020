
data = []
lista1 = []
lista2 = []

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi)

def teeListat():
    global lista1, lista2
    for rivi in data:
        a, b = rivi.split("   ")
        lista1.append(int(a))
        lista2.append(int(b))

    lista2 = sorted(lista2)
    lista1 = sorted(lista1)


def distances():
    dist = []
    for i in range(len(lista1)):
        dist.append(abs(lista1[i] - lista2[i]))

    print(sum(dist))


readfile()
teeListat()
distances()