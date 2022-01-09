from _pacman_class import *
import pygame

matriisi = []
korkeus = 100
leveys = 100
carts = []
carts_old = []
omenat = []     # @
syodyt_omenat = []  
pygame.init()

WHITE = (211, 211, 211)   
BLACK = (11, 11, 11)   
RED = (233, 3, 3)
GREEN = (3, 233, 3)
WIDTH = 900
HEIGHT = 600
vali = 18
font = pygame.font.SysFont("Arial", vali )
font_pac = pygame.font.SysFont("Arial", vali + 5)
pac = None



def readfile():
    global pac
    f = open("data_oma.txt", "r")  # e riviä
    i = 0
    for rivi in f:
        matriisi.append([])
        j = 0
        for merkki in rivi:            
            if merkki == ">":                
                pac = Pacman(j, i, merkki) 
                carts.append(pac)
                matriisi[-1].append("-")
            elif merkki == "^":   
                print("hep")             
                orkki = Pacman(j, i, merkki) 
                carts.append(orkki)
                matriisi[-1].append("-")
            elif merkki == "@":
                omenat.append([j, i])
                matriisi[-1].append(merkki)
            else:
                matriisi[-1].append(merkki)
            j += 1
        i += 1


def piirra_kartta():
    naytto.fill(BLACK)
    for r in range(korkeus-1):
        for s in range(leveys-1):
            teksti = font.render(matriisi[r][s], True, WHITE)
            naytto.blit(teksti, (2 + s * vali, 2 + r * vali))   


def osuiko_omenaan(c):
    for o in omenat:
        if o[1] == c.y and o[0] == c.x:
            print("osui")
            matriisi[c.y][c.x] = "-"
            syodyt_omenat.append(o)
    for o in syodyt_omenat:
        pygame.draw.rect(naytto,  BLACK, pygame.Rect(2 + c.x_wanha * vali, 6 + c.y_wanha * vali, vali, vali))
        teksti = font.render(matriisi[o[1]][o[0]], True, WHITE)
        naytto.blit(teksti, (2 + o[0] * vali, 2 + o[1] * vali))
    pygame.display.flip()        



def piirra(c, pac_kaantymispyynto):  
    if matriisi[c.y][c.x] == "+":
        c.next_direction(pac_kaantymispyynto)

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

    osuiko_omenaan(c)                

    #peita vanha:
    pygame.draw.rect(naytto,  BLACK, pygame.Rect(2 + c.x_wanha * vali, 2+ c.y_wanha * vali, vali, vali))
    teksti = font.render(matriisi[c.y_wanha][c.x_wanha], True, WHITE)
    naytto.blit(teksti, (2 + c.x_wanha * vali, 2 + c.y_wanha * vali))       

    # peita uuden paikan polku, sitten uusi symboli
    pygame.draw.rect(naytto,  BLACK, pygame.Rect(2+ c.x * vali, 2+ c.y * vali, vali, vali))
    teksti = font_pac.render(c.symboli, True, c.vari)
    naytto.blit(teksti, (2 + c.x * vali, 2 + c.y * vali))



def main():
    global carts
    for c in carts:
        piirra(c, pac.direction)
    pygame.display.flip() 
    kello.tick(1)  
    kesken = True
    tuhoa_nama = []
    pac_kaantymispyynto = pac.direction

    while kesken:      
        
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()  
            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP: # self.directions = [0, 1, 2, 3] # ylös, oik, alas, vas  
                    pac_kaantymispyynto = 0
                if tapahtuma.key == pygame.K_RIGHT: # self.directions = [0, 1, 2, 3] # ylös, oik, alas, vas      
                    pac_kaantymispyynto = 1
                if tapahtuma.key == pygame.K_DOWN: # self.directions = [0, 1, 2, 3] # ylös, oik, alas, vas      
                    pac_kaantymispyynto = 2
                if tapahtuma.key == pygame.K_LEFT: # self.directions = [0, 1, 2, 3] # ylös, oik, alas, vas      
                    pac_kaantymispyynto = 3                

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
                piirra(c, pac_kaantymispyynto)                    
                tuhoa_nama = []
            piirra(c, pac_kaantymispyynto)
                
          
        carts = carts_kopio[:]
        """
        if len(carts) == 1:
            pygame.display.flip() 
            kello.tick(50)    
            print(carts[0].x, carts[0].y)
            pygame.quit()   """
            

        pygame.display.flip() 
        kello.tick(5)   

     
    

readfile()
leveys= len(matriisi[0])
korkeus = len(matriisi)
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

piirra_kartta()  # tämä piirretään vain kerran
main()

