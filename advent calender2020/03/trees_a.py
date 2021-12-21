
# open squares (.) and trees (#)

data = []
montako = 0


def readfile():
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())   


def etsi_puut():
    global montako
    x = 3
    y = 1
    for i in range(len(data)-1):
        if data[y][x] == "#":
            montako += 1
        x += 3
        if x >= len(rivi):
            x -= len(rivi) 
        y += 1




readfile()
for rivi in data:
    print(rivi)
etsi_puut()
print(montako)