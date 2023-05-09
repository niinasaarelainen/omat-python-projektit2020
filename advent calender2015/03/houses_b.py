data = []
houses = []

def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
            data.append(rivi.strip())

def lue():
    global houses

    x_Santa = 0
    y_Santa = 0
    x_Robo = 0
    y_Robo = 0
    houses.append([x_Santa, y_Santa])
    vuoro = 0

    for rivi in data:
        for merkki in rivi:
            if vuoro % 2 == 0:
                if merkki == ">":
                    x_Santa += 1
                if merkki == "<":
                    x_Santa -= 1
                if merkki == "^":
                    y_Santa += 1
                if merkki == "v":
                    y_Santa -= 1
                if [x_Santa, y_Santa] not in houses:
                    houses.append([x_Santa, y_Santa])
            else:
                if merkki == ">":
                    x_Robo += 1
                if merkki == "<":
                    x_Robo -= 1
                if merkki == "^":
                    y_Robo += 1
                if merkki == "v":
                    y_Robo -= 1
                if [x_Robo, y_Robo] not in houses:
                    houses.append([x_Robo, y_Robo])            

            vuoro += 1


readfile()
print(data)
lue()
print(houses)
print(len(houses))