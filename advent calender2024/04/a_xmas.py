data = []
montako = 0
from collections import defaultdict

def readfile():
    f = open("data.txt", "r")   # data_1 = 18
    for rivi in f:
        data.append(rivi.strip())


def horizontal():
    global montako
    for rivi in data:
        montako += rivi.count("XMAS")
        montako += rivi.count("SAMX")

def vertical():
    global montako
    for x in range(len(data[0])):
        rivi = ""
        for y in range(len(data)):
            rivi += data[y][x]
        print(rivi)
        montako += rivi.count("XMAS")
        montako += rivi.count("SAMX")


def  diag():
    global montako

    diagonal1 = defaultdict(list) # For the top right to bottom left
    diagonal2 = defaultdict(list) # For the top left to bottom right
    for i in range(len(data)):
        for j in range(len(data)):
            diagonal1[i-j].append(data[i][j])
            diagonal2[i+j].append(data[i][j])

    print("diagonal1", diagonal1)

    v1 = ["".join(v) for v in diagonal1.values()]
    v2 = ["".join(v) for v in diagonal2.values()]

    for rivi in v1:
        montako += rivi.count("XMAS")
        montako += rivi.count("SAMX")  

    for rivi in v2:
        montako += rivi.count("XMAS")
        montako += rivi.count("SAMX")  
    


readfile()
horizontal()
vertical()
diag()

print(montako)