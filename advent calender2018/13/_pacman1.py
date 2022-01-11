from _pacman_class import *
import pygame

matriisi = []
korkeus = 0
leveys = 0
carts = []
orkit = []
omenat = []     # @
syodyt_omenat = []  
omenoita = 0
pygame.init()

kello = pygame.time.Clock()

WHITE = (211, 211, 211)   
BLACK = (11, 11, 11)   
RED = (233, 3, 3)
GREEN = (3, 233, 3)
ORANGE = (190, 190, 10)

WIDTH = 1080
HEIGHT = 444
vali_x = 14
vali_y = 23
font = pygame.font.SysFont("Arial", (vali_x + vali_y) // 2 + 2)
font_pac = pygame.font.SysFont("Arial", (vali_x + vali_y) // 2 + 2 )
pac = None
level = 1
naytto = None


def alkutoiminnot():
    global leveys, korkeus, matriisi,carts, orkit, omenat, syodyt_omenat, omenoita, naytto
    matriisi = []
    carts = []
    orkit = []
    omenat = []     # @
    syodyt_omenat = []  
    omenoita = 0
    readfile()
    leveys= len(matriisi[3]) 
    korkeus = len(matriisi)
    naytto = pygame.display.set_mode((WIDTH, HEIGHT))
    piirra_kartta()  # tämä piirretään vain kerran

    

def readfile():
    global pac, omenoita, matriisi    
    f = open( "level" + str(level) + ".txt", "r")  # e riviä
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
            if matriisi[r][s] == "@":
                teksti = font.render(matriisi[r][s], True, ORANGE)
                naytto.blit(teksti, (s * vali_x - 3, 2 + r * vali_y)) 
            else:    
                teksti = font.render(matriisi[r][s], True, WHITE)
                naytto.blit(teksti, (2 + s * vali_x, 2 + r * vali_y))   


def osuiko_omenaan(c):
    for o in omenat:
        if o[1] == c.y and o[0] == c.x:
            if matriisi[c.y][o[1] + 1] == "|" or matriisi[c.y][o[1 - 1]] ==  "|":
                matriisi[c.y][c.x] = "|"
            else:
                matriisi[c.y][c.x] = "-"
            syodyt_omenat.append(o)
            omenat.remove(o)
            if len(syodyt_omenat) == omenoita:
                next_level()
    pygame.display.flip()  


def piirra(c, pac_kaantymispyynto):  
    if c.y < korkeus and c.x < leveys:
        if matriisi[c.y][c.x] == "+":
            c.next_direction(pac_kaantymispyynto)

        if c == pac and matriisi[c.y][c.x] in ["D", "R"]:  # DANGER
            gameover()

        if c.symboli in [">", "<"]:                    
            if matriisi[c.y][c.x] == "\\":
                c.turn(1)
            if matriisi[c.y][c.x] ==  "/" :
                c.turn(-1)     
        
        elif c.symboli in ["v", "^"]:
            if matriisi[c.y][c.x] == "\\":
                c.turn(-1)
            if matriisi[c.y][c.x] ==  "/" :
                c.turn(1)    

        if c == pac:
            osuiko_omenaan(c)                

        #peita vanha:
        pygame.draw.rect(naytto,  BLACK, pygame.Rect(c.x_wanha * vali_x, 6 + c.y_wanha * vali_y, vali_x+2, vali_y+2))
        teksti = font.render(matriisi[c.y_wanha][c.x_wanha], True, WHITE)
        naytto.blit(teksti, (2 + c.x_wanha * vali_x, 2 + c.y_wanha * vali_y))       

        # peita uuden paikan polku, sitten uusi symboli
        pygame.draw.rect(naytto,  BLACK, pygame.Rect(c.x * vali_x, 6 + c.y * vali_y, vali_x+2, vali_y+2))
        teksti = font_pac.render(c.symboli, True, c.vari)
        naytto.blit(teksti, (2 + c.x * vali_x, 2 + c.y * vali_y))


def score():
    pygame.draw.rect(naytto,  BLACK, pygame.Rect(100, 52, vali_x + 5, vali_y + 5))
    teksti = font_pac.render(f"{len(syodyt_omenat)} / {omenoita} ", True, GREEN)
    naytto.blit(teksti, (100, 52))


def next_level():
    global level
    level += 1
    alkutoiminnot()


def main():                 ###    main   start          main   start   
    global carts
    for c in carts:
        piirra(c, pac.direction)
    pygame.display.flip() 
    kello.tick(1)  
    kesken = True
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
            missa_pac = orkki.missa_suunnassa_pac(pac)
            if missa_pac == "game_over":
                gameover()
            else:
                piirra(orkki, missa_pac)        
        
        pac.liiku()                                          
        piirra(pac, pac_kaantymispyynto)
        score()            

        pygame.display.flip() 
        for orkki in orkit: 
            if orkki.missa_suunnassa_pac(pac) == "game_over":  # pitää kaksi kertaa, jotteivat pac ja orkki vain
                gameover()                                      # vaihda paikkaa törmäämättä
        kello.tick(5)   
                                    ###    main    end        main   end   

def gameover():
    naytto.fill(BLACK)
    teksti = font_pac.render(f"  G A M E    O V E R ", True, ORANGE)
    naytto.blit(teksti, (300, HEIGHT // 2))
    pygame.display.flip() 
    pygame.time.delay(4000)
    alkutoiminnot()

    

alkutoiminnot()
main()

