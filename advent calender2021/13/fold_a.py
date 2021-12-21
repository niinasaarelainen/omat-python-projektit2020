import math

coordinates = []
height = 0
width = 0
ohje = ""


def readfile():   # a-kohta
    global coordinates,height, width, ohje
    
    f = open("data.txt", "r")         
    for rivi in f:
        if rivi.strip() == "":
            continue
        if "fold" in rivi:
            ohje = rivi.strip()
            break
        else:
            coordinates.append([])
            numerot_str = rivi.split(",")
            x = int(numerot_str[0])
            y = int(numerot_str[1].strip())
            coordinates[-1].append(x)
            if x > width:
                width = x
            coordinates[-1].append(y)
            if y > height:
                height = y 


def draw_co():
    global coordinates
    
    # empties
    for y in range(height + 1):
        for x in range(width + 1):
            if [x, y] in coordinates:
                print("#", end ="")
            else:
                print(".", end ="")
        print()
    print()


def fold():
    global height, coordinates, width
    ohje_split = ohje.split("=")
    fold_koord = int(ohje_split[1].strip()) 
    if "y" in ohje_split[0]:
        for i in range(len(coordinates)):
            y = coordinates[i][1]
            if y > fold_koord:
                distanssi = y - fold_koord
                coordinates[i][1] = coordinates[i][1] - 2 * distanssi
    
        if height % 2 == 1:
            height = height // 2
        else:
            height = height // 2 - 1
        
    else:
        for i in range(len(coordinates)):
            x = coordinates[i][0]
            if x > fold_koord:
                distanssi = x - fold_koord
                coordinates[i][0] = coordinates[i][0] - 2 * distanssi
    
        if width % 2 == 1:
            width = width // 2
        else:
            width = width // 2 - 1

    print(coordinates)
    uusi = []
    [uusi.append(x) for x in coordinates if x not in uusi]
    print(len(uusi))


readfile()
print(coordinates, ohje)
#draw_co()
fold()
#draw_co()
