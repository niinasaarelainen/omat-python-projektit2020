from cart_class import *
import pygame

matriisi = []
carts = []
pygame.init()
font = pygame.font.SysFont("Arial", 30)
WHITE = (211, 211, 211)   
BLACK = (11, 11, 11)   
WIDTH = 700 
HEIGHT = 200



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
            if merkki == "<":                
                carts.append(Cart(j, i, 3) )
            j += 1
        i += 1

    #test:
    carts.append(Cart(1, 0, 1) )   # 1 = myötäpäivään
    carts.append(Cart(2, 0, -1) )  # -1 = vastapäivään

def luo_matriisi():
    for r in range(korkeus):
        matriisi.append([])
        for s in range(leveys):
            matriisi[-1].append('.')

def piirra(c):
    for r in range(korkeus):
        for s in range(leveys):
            teksti = font.render(matriisi[r][s], True, WHITE)
            naytto.blit(teksti, (50 + s * 20, 10 + r*30))   

            if c.x == s and c.y == r:
                if matriisi[r][s] in ["\\",  "/"] :
                    c.turn()     
                     
            teksti = font.render(c.symboli, True, WHITE)
            naytto.blit(teksti, (50 + c.x * 20, 10 + c.y*30))



def main():

    for c in carts:
        piirra(c)

    kesken = True
    while kesken:        
        naytto.fill(BLACK)
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()  

        for c in carts:
            #if c.y == korkeus -1 and c.x == leveys -1:
            #    kesken = False 
            c.liiku()
            piirra(c)

        pygame.display.flip() 
        kello.tick(3)   

    print("END")
    

readfile()
leveys= len(matriisi[-1])
korkeus = len(matriisi)
print(korkeus, leveys)
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

main()

