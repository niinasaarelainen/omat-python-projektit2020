data = []
houses = []

def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
            data.append(rivi.strip())

def lue():
    global houses

    x = 0
    y = 0
    houses.append([x, y])

    for rivi in data:
        for merkki in rivi:
            print(merkki)
            if merkki == ">":
                x += 1
            if merkki == "<":
                x -= 1
            if merkki == "^":
                y += 1
            if merkki == "v":
                y -= 1
        
            if [x, y] not in houses:
                houses.append([x, y])


readfile()
print(data)
lue()
print(houses)
print(len(houses))