
data = {}
data_vaarinpain = {}
luvut = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        k, v = rivi.split(")")
        if k in data:
            data[k].append(v.strip())    # voi olla "monta planeettaa"
        else:
            data[k] = [v.strip()]
        
        data_vaarinpain[v.strip()] = k    # orbitoi vain yhden ympäri

    print(data)


def tutki():
    orbits = 0
    for k, values in data.items():
        for v in values:
            print(" v: ", v)
            while v != 'COM':
                print(k)
                v = data_vaarinpain[v]
                orbits += 1

    return orbits



readfile()
print(tutki())  # 171213

"""      G - H       J - K - L
        /           /
 COM - B - C - D - E - F
                \
                 I                          """