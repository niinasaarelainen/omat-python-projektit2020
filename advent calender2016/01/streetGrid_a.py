
data = []



def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        items = (rivi.strip().split(", "))
        for item in items:
            data.append(item)


def laske():
    x = 0
    y = 0
    suunta = 0  

    for rivi in data:
        ilmansuunta = (rivi[:1])  # L tai R
        paljonko = int((rivi[1:]))  # luku 1-192
        if ilmansuunta == 'R':
            suunta += 1
        if ilmansuunta == 'L':
            suunta += 3
        suunta = suunta % 4

        if suunta == 1:
            x += paljonko
        if suunta == 2:
            y -= paljonko
        if suunta == 3:
            x -= paljonko
        if suunta == 0:
            y += paljonko
    
    return abs(x) + abs(y)



readfile()
print(laske())
