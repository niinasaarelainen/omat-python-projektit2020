data = []
ohje = ""
puu = {}


def readfile():   # a-kohta
    f = open("data.txt", "r")  
    for rivi in f:
        data.append(rivi.strip()) 
    
def kasittele_data():
    global ohje
    ohje = data[0]
    for rivi in data[2:]:
        node, lr = rivi.split(" = ")
        l, r = lr.split(", ")
        puu[node] = [l[1:], r[:-1]]
            

def lue_ohjeet():
    olet_tassa = "AAA"
    sijainnit = []
    while olet_tassa != "ZZZ":
        for kirjain in ohje:
            if olet_tassa == "ZZZ":
                return len(sijainnit)
            if kirjain == "L":
                olet_tassa = puu[olet_tassa][0]
            else:
                olet_tassa = puu[olet_tassa][1]

            print(olet_tassa)
            sijainnit.append(olet_tassa)

    return len(sijainnit)


readfile()
kasittele_data() 
print(puu)
print(lue_ohjeet())