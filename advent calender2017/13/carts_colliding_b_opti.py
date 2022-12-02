from cart_class import *
import pygame

matriisi = []
carts = []
carts_old = []
pygame.init()

WHITE = (211, 211, 211)   
BLACK = (11, 11, 11)   
RED = (233, 3, 3)
WIDTH = 1200
HEIGHT = 1200
vali = 19
font = pygame.font.SysFont("Arial", vali )



def readfile():
    f = open("data.txt", "r")  # e riviä
    i = 0
    for rivi in f:
        matriisi.append([])
        j = 0
        for merkki in rivi:
            
            if merkki == ">":                
                carts.append(Cart(j, i, merkki) )
                matriisi[-1].append("-")
            elif merkki == "<":                
                carts.append(Cart(j, i, merkki) )
                matriisi[-1].append("-")
            elif merkki == "v":                
                carts.append(Cart(j, i, merkki) )
                matriisi[-1].append("|")
            elif merkki == "^":                
                carts.append(Cart(j, i, merkki) )
                matriisi[-1].append("|")
            else:
                matriisi[-1].append(merkki)
            j += 1
        i += 1

    #test:
    #carts.append(Cart(3, 0, ">") )  
    #carts.append(Cart(9, 3, "v") )  
    #carts.append(Cart(5, 5, ">") )  
    #carts.append(Cart(4, 0, "<") )  


def piirra_kartta():
    naytto.fill(BLACK)
    for r in range(korkeus):
        for s in range(leveys):
            teksti = font.render(matriisi[r][s], True, WHITE)
            naytto.blit(teksti, (2 + s * vali, 2 + r * vali))   


def piirra(c):    

    if matriisi[c.y][c.x] == "+":
        c.next_direction()

    if c.symboli in [">", "<"]:                    
        if matriisi[c.y][c.x] == "\\":
            c.turn(1)
        if matriisi[c.y][c.x] ==  "/" :
            c.turn(-1)     
    
    elif c.symboli in["v", "^"]:
        if matriisi[c.y][c.x] == "\\":
            c.turn(-1)
        if matriisi[c.y][c.x] ==  "/" :
            c.turn(1)    

    #peita vanha:
    pygame.draw.rect(naytto,  BLACK, pygame.Rect(2 + c.x_wanha * vali, 2+ c.y_wanha * vali, vali, vali))
    teksti = font.render(matriisi[c.y_wanha][c.x_wanha], True, WHITE)
    naytto.blit(teksti, (2 + c.x_wanha * vali, 2 + c.y_wanha * vali))       

    # peita uuden paikan polku, sitten uusi symboli
    pygame.draw.rect(naytto,  BLACK, pygame.Rect(2+ c.x * vali, 2+ c.y * vali, vali, vali))
    teksti = font.render(c.symboli, True, RED)
    naytto.blit(teksti, (2 + c.x * vali, 2 + c.y * vali))



def main():
    global carts
    for c in carts:
        piirra(c)
    pygame.display.flip() 
    kello.tick(1)  

    kesken = True
    tuhoa_nama = []
    while kesken:       
        
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()  

        carts.sort(key = lambda x: (x.y, x.x))
        carts_kopio = carts[:]
        
        for c in carts:
            c.liiku()            
            for c_verrokki in carts:
                if c.x == c_verrokki.x and c.y == c_verrokki.y and c is not c_verrokki:
                    print("HIT")
                    if c not in tuhoa_nama:
                        tuhoa_nama.append(c)
                    if c_verrokki not in tuhoa_nama:
                        tuhoa_nama.append(c_verrokki)
            for tuhottava in tuhoa_nama:
                carts_kopio.remove(tuhottava)
                tuhottava.symboli = "X"                    
                piirra(c)                    
                tuhoa_nama = []
            piirra(c)
                
          
        carts = carts_kopio[:]
        
        if len(carts) == 1:
            pygame.display.flip() 
            kello.tick(50)    
            print(carts[0].x, carts[0].y)
            pygame.quit()  
            

        pygame.display.flip() 
        kello.tick(100)   

     
    

readfile()
leveys= len(matriisi[-1])
korkeus = len(matriisi)
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

piirra_kartta()  # tämä piirretään vain kerran
main()

