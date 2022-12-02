
data = []
leveys =  25
korkeus = 6
layer = leveys * korkeus
layers = []

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def muodosta_layerit():
    global layer, layers
    for i in range(len(data[0]) // layer):
        layers.append(data[0][i * layer: (i + 1) * layer])

    return layers

"""
0 black
1 white
2 (transparent)
"""

def tutki_layerit():
    global layers
    final_layer = []
    #print(layers[0])
    for nro in range(len(layers[0])):
        lisatty = False
        for l in layers:
            if l[nro] in ["0", "1"] :
                final_layer.append(l[nro])
                lisatty = True
                break

        if lisatty == False:
            final_layer.append("2")


    return final_layer


readfile()
print(muodosta_layerit())
l = tutki_layerit()
rivinvaihto = 0
for j in range(len(l)):
    print(l[j], end="")
    rivinvaihto += 1
    if rivinvaihto == leveys:
        print()
        rivinvaihto = 0

