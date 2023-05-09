
data = []



def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        data.append(rivi)


def laske():

    floor = 0
    position = 0

    for rivi in data:
        for merkki in rivi:
            position += 1
            if merkki == "(":
                floor += 1
            if merkki == ")":
                floor -= 1
            if floor < 0:
                return position



readfile()
print(laske())
