
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


def tutki(value):
    
    v = data_vaarinpain[value]
    reitti = [v]
    #print(" v: ", v)
    while v != 'COM':
        reitti.append(data_vaarinpain[v])
        v = data_vaarinpain[v]

    return reitti


def tutki_yhteiset(reitti1, reitti2):
    ind1 = 0
    ind2 = 0
    for kirjain in reitti2:
        if kirjain in reitti1:
            ind1 = reitti1.index(kirjain)
            ind2 = reitti2.index(kirjain)
            break
    print(ind1+ind2)



readfile()
reitti1 = tutki("YOU") 
reitti2 = tutki("SAN") 
tutki_yhteiset(reitti1, reitti2)

"""                             
                         YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN             """