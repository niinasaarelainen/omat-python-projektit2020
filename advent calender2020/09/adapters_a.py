import math

data = [0]
highest = 0
one_jolt_differences = 0
three_jolt_differences = 0

def readfile():   # a-kohta
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(int(rivi.strip()))
    highest = max(data) + 3
    data.append(highest)
    data.sort()
    print(data)
   

def laske_erotukset():
    erotukset = []
    for i in range(len(data) -1):
        erotukset.append(data[i + 1] - data[i])

    print(erotukset)
    ykkoset = erotukset.count(1)
    kolmoset = erotukset.count(3)
    print(ykkoset * kolmoset)





readfile()
laske_erotukset()   