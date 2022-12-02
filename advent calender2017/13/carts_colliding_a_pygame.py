from cart_class import *
import pygame

matriisi = []
carts = []
pygame.init()
font = pygame.font.SysFont("Arial", 30)
WHITE = (211, 211, 211)   
BLACK = (11, 11, 11)   
WIDTH = 300
HEIGHT = 300



def readfile():
    f = open("data_easy2.txt", "r")  # e riviä
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

def luo_matriisi():
    for r in range(korkeus):
        matriisi.append([])
        for s in range(leveys):
            matriisi[-1].append('.')

def piirra(c):
    for r in range(korkeus):
        for s in range(leveys):
            teksti = font.render(matriisi[r][s], True, WHITE)
            naytto.blit(teksti, (50 + s * 20, 10 + r * 30))   

            if c.x == s and c.y == r:
                if matriisi[r][s] == "+":
                    c.next_direction()

                if c.symboli in [">", "<"]:                    
                    if matriisi[r][s] == "\\":
                        c.turn(1)
                    if matriisi[r][s] ==  "/" :
                        c.turn(-1)     
                
                elif c.symboli in["v", "^"]:
                    if matriisi[r][s] == "\\":
                        c.turn(-1)
                    if matriisi[r][s] ==  "/" :
                        c.turn(1) 
                
                     
            teksti = font.render(c.symboli, True, WHITE)
            naytto.blit(teksti, (50 + c.x * 20, 10 + c.y*30))



def main():
    global carts
    for c in carts:
        piirra(c)
    pygame.display.flip() 
    kello.tick(2)  

    kesken = True
    tuhoa_nama = []
    while kesken:        
        naytto.fill(BLACK)
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()  

        
        carts_kopio = carts[:]
        jatketaan = True
        carts.sort(key = lambda x: (x.y, x.x))
        for c in carts:
            if jatketaan:
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
                    print(c.x, c.y)
                    piirra(c)
                    pygame.quit() 
                    tuhoa_nama = []
                    jatketaan = False
                piirra(c)
          
        carts = carts_kopio[:]
        """        if len(carts) == 0:
            pygame.display.flip() 
            kello.tick(50)    """
            

        pygame.display.flip() 
        kello.tick(2)   

     
    

readfile()
leveys= len(matriisi[-1])
korkeus = len(matriisi)
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

main()

