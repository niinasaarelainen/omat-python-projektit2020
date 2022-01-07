from cart_class import *

matriisi = []
leveys= 8
korkeus = 8 
data = []

def readfile():
    global olet_nyt_tassa_x, olet_nyt_tassa_y
    f = open("data_easy2.txt", "r") 
    i = 0
    for rivi in f:
        data.append([])
        j = 0
        for merkki in rivi.strip():
            data[-1].append(merkki)
            if merkki == "@":
                olet_nyt_tassa_y = i
                olet_nyt_tassa_x = j
            j += 1
        i += 1

def luo_matriisi():
    for r in range(korkeus):
        matriisi.append([])
        for s in range(leveys):
            matriisi[-1].append('.')

def piirra(c1):
    tyhjenna_matriisi()
    print()
    matriisi[c1.y][c1.x] = "@"
    for r in range(korkeus):
        print(matriisi[r])

def tyhjenna_matriisi():
    for r in range(korkeus):
        for s in range(leveys):
            matriisi[r][s] = '.'

def luo_carts():
    c1 = Cart(3, 4, 1)    
    piirra(c1)
    c1.liiku()
    piirra(c1)
    c1.next_direction()
    c1.liiku()
    print("next_direction: L")
    piirra(c1)
    c1.liiku()
    piirra(c1)
    c1.next_direction()
    c1.liiku()
    print("next_direction: ei muutosta")
    piirra(c1)
    c1.liiku()
    piirra(c1)
    c1.next_direction()
    c1.liiku()
    print("next_direction: R")
    piirra(c1)
    c1.liiku()
    piirra(c1)
    c1.next_direction()
    c1.liiku()
    print("next_direction: L")
    piirra(c1)
    c1.liiku()
    piirra(c1)



#readfile()
#print(data)
luo_matriisi()
luo_carts()  # 0 askelta

