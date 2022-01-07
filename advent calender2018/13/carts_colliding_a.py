from cart_class import *

matriisi = []
leveys= 10
korkeus = 10 
data = []
carts = []

def readfile():
    global olet_nyt_tassa_x, olet_nyt_tassa_y
    f = open("data_easy.txt", "r")  # e riviä
    i = 0
    for rivi in f:
        data.append([])
        j = 0
        for merkki in rivi.strip():
            data[-1].append(merkki)
            if merkki == ">":
                olet_nyt_tassa_y = i
                olet_nyt_tassa_x = j
            j += 1
        i += 1

def luo_matriisi():
    for r in range(korkeus):
        matriisi.append([])
        for s in range(leveys):
            matriisi[-1].append('.')

def piirra(carts):
    tyhjenna_matriisi()
    print()
    for c in carts:
        matriisi[c.y][c.x] = c.symboli
    for r in range(korkeus):
        print(matriisi[r])

def tyhjenna_matriisi():
    for r in range(korkeus):
        for s in range(leveys):
            matriisi[r][s] = '.'

def luo_carts():
    c1 = Cart(3, 3, 2)   # [0, 1, 2, 3] # ylös, oik, alas, vas 
    c2 = Cart(3, 5, 0)  
    carts.append(c1)
    carts.append(c2)
    piirra(carts)
    
    for i in range(15):  
        for c in carts:            
            print(c.kaantosuunta)
            c.liiku()   
            if c1.x == c2.x and c1.x == c2.x:
                print("törmäys !!!!!!!!!!") 
            print("next_direction: L")
            piirra(carts)
            c.next_direction()
            c.liiku()
            piirra(carts)  



#readfile()
#print(data)
luo_matriisi()
luo_carts()  # 0 askelta

