from cart_class import *

matriisi = []
carts = []

def readfile():
    f = open("data_easy.txt", "r")  # e riviä
    i = 0
    for rivi in f:
        matriisi.append([])
        j = 0
        for merkki in rivi:
            matriisi[-1].append(merkki)
            if merkki == ">":                
                carts.append(Cart(j, i, 1) )
            j += 1
        i += 1

def luo_matriisi():
    for r in range(korkeus):
        matriisi.append([])
        for s in range(leveys):
            matriisi[-1].append('.')

def piirra(carts):
    #tyhjenna_matriisi()
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
    piirra(carts)
    
    

readfile()
leveys= len(matriisi[-1])
korkeus = len(matriisi)
luo_carts()  

