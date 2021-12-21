
xy_parit = []
varatut_koordinaatit = {}

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        xy_parit.append(rivi.split("->"))


def kasittele_tunniste(tunniste):
    if tunniste in varatut_koordinaatit:
        varatut_koordinaatit[tunniste] += 1
    else:
        varatut_koordinaatit[tunniste] = 1

def kasittele_xy_parit():
    for pari in xy_parit:
            x1 = int(pari[0].split(",")[0].strip())
            y1 = int(pari[0].split(",")[1].strip())
            x2 = int(pari[1].split(",")[0].strip())
            y2 = int(pari[1].split(",")[1].strip())
            xt = [x1,x2]
            xt.sort()
            yt = [y1,y2]
            yt.sort()

            if y1 == y2:                
                for x in range(xt[0], xt[1] + 1):
                    tunniste = str(x) + "." + str(y1)
                    kasittele_tunniste(tunniste)
            elif x1 == x2:                
                for y in range(yt[0], yt[1] + 1):
                    tunniste =  str(x1) + "." + str(y)
                    kasittele_tunniste(tunniste)
            else:
                lisa = 0
                for x in range(xt[0], xt[1] + 1):
                    if x1 > x2 and y1 > y2:
                        tunniste =  str(x1 - lisa) + "." + str(y1 - lisa)
                    elif x1 < x2 and y1 > y2:
                        tunniste =  str(x1 + lisa) + "." + str(y1 - lisa)
                    elif x1 > x2 and y1 < y2:
                        tunniste =  str(x1 - lisa) + "." + str(y1 + lisa)
                    else: 
                        tunniste =  str(x1 + lisa) + "." + str(y1 + lisa)
                    kasittele_tunniste(tunniste)
                    lisa += 1

def montako_duplikaattia():
    dupli = [ item  for item in varatut_koordinaatit.items() if item[1] > 1 ]
    print(len(dupli))


readfile()
print(xy_parit)   # ['0,9 ', ' 5,9\n']
kasittele_xy_parit()
montako_duplikaattia()