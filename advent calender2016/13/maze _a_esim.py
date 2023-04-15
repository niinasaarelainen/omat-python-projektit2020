data = 1358   # oikea
data = 10     # esim
kuva = []
mina_x = 1
mina_y = 1
kohde_x = 7
kohde_y = 4
reitti = []   # minan liikkeet talteen, jotta voi pakittaa
jumissa = 0


def alusta_kuva():
    for y in range(7):    # mallissa 7 riviä, oikeasti ???
        rivi = []
        for x in range(10):
            rivi.append(0)
        kuva.append(rivi)


def open_or_wall(y, x):
    luku = (x*x + 3*x + 2*x*y + y + y*y) + data
    b = bin(luku)[2:]
    s = sum([int(luku) for luku in b])
    kuva[y][x] = s % 2
    kuva[mina_y][mina_x] = "M"

def print_kuva():
    print()
    #talteen = kuva[mina_y][mina_x]   
    for rivi in kuva:
        for x in rivi:
            print(x, end="")
        print()
    #kuva[mina_y][mina_x] = talteen


def liiku():
    global mina_x, mina_y, jumissa
    x_matka = kohde_x - mina_x
    y_matka = kohde_y - mina_y
    print("y_matka", y_matka, "x_matka", x_matka)
    if abs(y_matka) == max(abs(x_matka), abs(y_matka)):
        if y_matka > 0:
            liike = 1
        else:
            print("nega")
            liike = -1
        if kuva[mina_y + liike][mina_x] == 0:
            mina_y += liike
        elif kuva[mina_y][mina_x + 1] == 0:     # muuta tämäkin ??
            mina_x += 1
    elif abs(x_matka) == max(abs(x_matka), abs(y_matka)):
        if x_matka > 0:
            liike = 1
        else:
            liike = -1
        if kuva[mina_y][mina_x + liike] == 0:
            mina_x += liike
        elif kuva[mina_y + 1][mina_x] == 0:  # muuta tämäkin ??
            mina_y += 1
    
    if len(reitti) > 0:
        mina_y_vika, mina_x_vika = reitti[-1]
        
        if mina_x_vika == mina_x and mina_y_vika == mina_y:
            print("jumissa")
            jumissa += 1
            #print("mina_y_vika:", mina_y_vika, "mina_x_vika:", mina_x_vika)
            mina_y_vika2, mina_x_vika2 = reitti[-2]
            #print("mina_y_vika2:", mina_y_vika2, "mina_x_vika2:", mina_x_vika2)
            y_erotus = abs(mina_y_vika2 - mina_y_vika)
            x_erotus = abs(mina_x_vika2 - mina_x_vika)
            #print("y_erotus:", y_erotus, "x_erotus", x_erotus)
            if y_erotus > 0:
                mina_x += 1
                mina_y = mina_y_vika2   # 2.vika arvo
            if x_erotus > 0:
                mina_y += 1
                mina_x = mina_x_vika2   # 2.vika arvo
        #del reitti[-1]   ?? miksei toimi reitti.pop(-1) ei myöskään  ?!?!?!?
        reitti.append([mina_y, mina_x])
    if len(reitti) == 0:
        reitti.append([mina_y, mina_x])


##   MAIN   ##
alusta_kuva()
for y in range(7):
    for x in range(10):
        open_or_wall(y, x)

for x in range(16):    
    liiku()
    kuva[mina_y][mina_x] = "M"
    if mina_y == kohde_y and mina_x == kohde_x:  # 7,4
        print("HIT")
        break

print_kuva()
print(reitti)
print(len(reitti) - jumissa)