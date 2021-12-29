
data = []
facing = "E"
suunnat = ["N", "E", "S", "W"]
ship_x = 0
ship_y = 0

def readfile():   # a-kohta
    global data
    f = open("data.txt", "r")         
    for rivi in f:
        ohje = rivi[:1]
        nro  = int(rivi[1:].strip())
        data.append([ohje, nro])
    print(data) 


def lue_ohjeet():
    global ship_x , ship_y, facing
    for ohje, nro in data:

        if ohje == "F":
            if facing == "E":
                ship_x += nro
            if facing == "W":
                ship_x -= nro
            if facing == "N":
                ship_y += nro
            if facing == "S":
                ship_y -= nro

        if ohje == "N":
            ship_y += nro

        if ohje == "S":
            ship_y -= nro

        if ohje == "W":
            ship_x -= nro

        if ohje == "E":
            ship_x += nro

        if ohje == "R":
            ind = suunnat.index(facing)
            steps = nro // 90
            facing = suunnat[(ind + steps) % 4]
            print(facing)

        if ohje == "L":
            ind = suunnat.index(facing)
            steps = nro // 90
            facing = suunnat[(ind - steps) % 4]
            print(facing)

        print(ship_x , ship_y)

    return(abs(ship_x), abs(ship_y))
    



readfile()
x, y = lue_ohjeet()
print(x + y)