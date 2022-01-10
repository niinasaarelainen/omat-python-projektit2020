from _pacman_class import *
import pygame

matriisi = []
korkeus = 0
leveys = 0
carts = []
carts_old = []
orkit = []
omenat = []     # @
syodyt_omenat = []  
omenoita = 0
pygame.init()

WHITE = (211, 211, 211)   
BLACK = (11, 11, 11)   
RED = (233, 3, 3)
GREEN = (3, 233, 3)
WIDTH = 1080
HEIGHT = 444
vali_x = 14
vali_y = 23
font = pygame.font.SysFont("Arial", (vali_x + vali_y) // 2 )
font_pac = pygame.font.SysFont("Arial", vali_y + 3)
pac = None



def readfile():
    global pac, omenoita
    f = open("level1.txt", "r")  # e riviä
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
                orkki = Pacman(j, i, merkki) 
                orkit.append(orkki)
                carts.append(orkki)
                matriisi[-1].append("|")
            elif merkki == "@":
                omenat.append([j, i])
                matriisi[-1].append(merkki)
            else:
                matriisi[-1].append(merkki)
            j += 1
            if j == 77:
                break
        i += 1

    omenoita = len(omenat)


def piirra_kartta():
    naytto.fill(BLACK)
    for r in range(korkeus):
        for s in range(leveys):
            print(r, s)
            teksti = font.render(matriisi[r][s], True, WHITE)
            naytto.blit(teksti, (2 + s * vali_x, 2 + r * vali_y))   


def osuiko_omenaan(c):
    for o in omenat:
        if o[1] == c.y and o[0] == c.x:
            print("osui")
            matriisi[c.y][c.x] = "-"
            syodyt_omenat.append(o)
            if len(syodyt_omenat) == omenoita:
                next_level()
            omenat.remove(o)
    for o in syodyt_omenat:
        pygame.draw.rect(naytto,  BLACK, pygame.Rect(2 + c.x_wanha * vali_x, 6 + c.y_wanha * vali_y, vali_x, vali_y))
        teksti = font.render(matriisi[o[1]][o[0]], True, WHITE)
        naytto.blit(teksti, (2 + o[0] * vali_x, 2 + o[1] * vali_y))
    pygame.display.flip()        



def piirra(c, pac_kaantymispyynto):  
    if c.y < korkeus and c.x < leveys:
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
        pygame.draw.rect(naytto,  BLACK, pygame.Rect(2 + c.x_wanha * vali_x, 6 + c.y_wanha * vali_y, vali_x, vali_y))
        teksti = font.render(matriisi[c.y_wanha][c.x_wanha], True, WHITE)
        naytto.blit(teksti, (2 + c.x_wanha * vali_x, 2 + c.y_wanha * vali_y))       

        # peita uuden paikan polku, sitten uusi symboli
        pygame.draw.rect(naytto,  BLACK, pygame.Rect(2+ c.x * vali_x, 6 + c.y * vali_y, vali_x, vali_y))
        teksti = font_pac.render(c.symboli, True, c.vari)
        naytto.blit(teksti, (2 + c.x * vali_x, 2 + c.y * vali_y))


def score():
        pygame.draw.rect(naytto,  BLACK, pygame.Rect(100, 15, vali_x + 5, vali_y + 5))
        teksti = font_pac.render(f"{len(syodyt_omenat)} / {omenoita} ", True, GREEN)
        naytto.blit(teksti, (100, 52))


def next_level():
    print("next_level")

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


        for orkki in orkit:            
            orkki.liiku()
            piirra(orkki, orkki.missa_suunnassa_pac(pac))        
        
        pac.liiku() 
        piirra(pac, pac_kaantymispyynto)

        score()

                
        
        """
        if len(carts) == 1:
            pygame.display.flip() 
            kello.tick(50)    
            print(carts[0].x, carts[0].y)
            pygame.quit()   """
            

        pygame.display.flip() 
        kello.tick(5)   

     
    

readfile()
leveys= len(matriisi[3]) 
korkeus = len(matriisi)
print(leveys, korkeus)
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

piirra_kartta()  # tämä piirretään vain kerran
main()

