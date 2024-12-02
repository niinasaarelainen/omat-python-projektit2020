data = []  
y_muistiin = []
x_muistiin = []
data_numerot = []
coordinates = {}

times =  1000000 -1


def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())


def etsi_tyhjat():
    global y_muistiin, x_muistiin

    # rivit
    for y in range(len(data)):
        if "#" not in data[y]:
            y_muistiin.append(y)

    # sarakkeet
    for x in range(len(data[0])):
        sarake = list([data[y][x] for y in range(len(data))])
        if "#" not in sarake:
            x_muistiin.append(x)



def unique_number():
    nro = 1
    monesko_y = 0
    for y in range(len(data)):
        uusi_rivi = []
        monesko_x = 0
        if y in y_muistiin:
            monesko_y += 1
        for x in range(len(data[0])):
            if x in x_muistiin:
                monesko_x += 1
            if data[y][x] == '#':
                uusi_rivi.append(nro)
                coordinates[nro] = [y + monesko_y * times, x + monesko_x * times]
                nro += 1
            else:
                uusi_rivi.append(data[y][x])
        data_numerot.append(uusi_rivi)   

def pairs():
    sum = 0
    for k1 in coordinates:
        for k2 in range(k1+1, len(coordinates) +1):
            sum += abs(coordinates[k1][0] - coordinates[k2][0]) + abs(coordinates[k1][1] - coordinates[k2][1])
    print(sum)


readfile()
etsi_tyhjat()
print(x_muistiin, y_muistiin)

unique_number()
print(data_numerot)
print(coordinates)

pairs()