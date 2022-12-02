
xy_parit = []
varatut_koordinaatit = {}

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        xy_parit.append(rivi.split("->"))


def kasittele_xy_parit():
    for pari in xy_parit:
            x1 = int(pari[0].split(",")[0].strip())
            y1 = int(pari[0].split(",")[1].strip())
            x2 = int(pari[1].split(",")[0].strip())
            y2 = int(pari[1].split(",")[1].strip())
            if y1 == y2:
                xt = [x1,x2]
                xt.sort()
                for x in range(xt[0], xt[1] + 1):
                    tunniste = str(x) + "." + str(y1)
                    if tunniste in varatut_koordinaatit:
                        varatut_koordinaatit[tunniste] += 1
                    else:
                        varatut_koordinaatit[tunniste] = 1
            if x1 == x2:
                yt = [y1,y2]
                yt.sort()
                for y in range(yt[0], yt[1] + 1):
                    tunniste =  str(x1) + "." + str(y)
                    if tunniste in varatut_koordinaatit:
                        varatut_koordinaatit[tunniste] += 1
                    else:
                        varatut_koordinaatit[tunniste] = 1

def montako_duplikaattia():
    dupli = [ item  for item in varatut_koordinaatit.items() if item[1] > 1 ]
    print(len(dupli))


readfile()
print(xy_parit)   # ['0,9 ', ' 5,9\n']
kasittele_xy_parit()
montako_duplikaattia()