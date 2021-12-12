import math

data = []  # strings


def readfile():   # a-kohta
    global data
    f = open("data_easy.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())
    print(data)


readfile()
()
