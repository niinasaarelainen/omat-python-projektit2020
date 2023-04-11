
data = []
locations = []


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
    locations.append((x, y))   

    for rivi in data:
        ilmansuunta = (rivi[:1])  # L tai R
        paljonko = int((rivi[1:]))  # luku 1-192
        if ilmansuunta == 'R':
            suunta += 1
        if ilmansuunta == 'L':
            suunta += 3
        suunta = suunta % 4
        

        if suunta == 1:
            for i in range(paljonko):
                x += 1
                if ((x, y)) in locations:
                    return abs(x) + abs(y)
                else:
                    locations.append((x, y))  
        if suunta == 2:
            for i in range(paljonko):
                y -= 1
                if ((x, y)) in locations:
                    return abs(x) + abs(y)
                else:
                    locations.append((x, y))  
        if suunta == 3:
           for i in range(paljonko):
                x -= 1
                if ((x, y)) in locations:
                    return abs(x) + abs(y)
                else:
                    locations.append((x, y))  
        if suunta == 0:
            for i in range(paljonko):
                y += 1
                if ((x, y)) in locations:
                    return abs(x) + abs(y)
                else:
                    locations.append((x, y))  

        print(locations, suunta)
        


readfile()
print(laske())
