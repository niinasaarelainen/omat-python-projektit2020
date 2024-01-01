import math

data = []  
data_expanded1 = []  
data_expanded2 = []  
data_numerot = []
coordinates = {}

times =  1000000 -1


def readfile():   
    f = open("data_1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())


def etsi_tyhjat():
    for rivi in data:
        if "#" not in rivi:
            for montako in range(times):    # !!!!!!!!!!!!!! # toimii jos 100, miljoonalla jumittaa jo 
                data_expanded1.append(list(rivi))   # tässä. Ei pääse printtaan pairs():ssa
        data_expanded1.append(list(rivi))

    # sarakkeet
    x_muistiin = []
    for x in range(len(data[0])):
        sarake = list([data[y][x] for y in range(len(data))])
        if "#" not in sarake:
            x_muistiin.append(x)
   
    return x_muistiin


def lisaa_sarakkeet(s_list):
    for y in range(len(data_expanded1)):
        uusi_rivi = []
        for x in range(len(data_expanded1[0])):
            if x in s_list:
                for montako in range(times):      # !!!!!!!!!!!
                    uusi_rivi.append('.')
            uusi_rivi.append(data_expanded1[y][x])
        data_expanded2.append(uusi_rivi)    

def unique_number():
    nro = 1
    for y in range(len(data_expanded2)):
        uusi_rivi = []
        for x in range(len(data_expanded2[0])):
            if data_expanded2[y][x] == '#':
                uusi_rivi.append(nro)
                coordinates[nro] = [y, x]
                nro += 1
            else:
                uusi_rivi.append(data_expanded2[y][x])
        data_numerot.append(uusi_rivi)   

def pairs():
    sum = 0
    for k1 in coordinates:
        for k2 in range(k1+1, len(coordinates) +1):
            print(k1, k2)
            sum += abs(coordinates[k1][0] - coordinates[k2][0]) + abs(coordinates[k1][1] - coordinates[k2][1])
    print(sum)


readfile()
sar = etsi_tyhjat()
"""
for rivi in data_expanded1:
    print(rivi) """
#print()
lisaa_sarakkeet(sar)
"""
for rivi in data_expanded2:
    print(rivi) """
print(len(data_expanded2[0]))

unique_number()
print()
print(coordinates)

pairs()