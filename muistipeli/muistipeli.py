import random, pygame
import glob


def lataa_kuvat():
    i = 0
    for filename in glob.iglob('t:/python/climbing_olympics_luokat/kiipeilijoiden_kuvat' + '**/*.png', recursive=True):
        kuva = pygame.image.load(filename)
        kuva = pygame.transform.scale(kuva, (90, 111) )
        kuvat.append(kuva) 
        r = random.randint(0, len(kuvat)-1)
        kuvat.insert(r, kuva)
        

def piirra(valinnat): 
    for valinta in valinnat:
        y = 0
        x = 0
        for kuva in kuvat:
            naytto.blit(kuva, (x * VALI_X, y * VALI_Y))
            x += 1
            if x == 10:
                y += 1
                x = 0        

def mika_kuva(x, y):
    x_ind = x // VALI_X
    y_ind = y // VALI_Y
    return x_ind, y_ind

def tutki_valinnat(valinnat):  # valinat = x, y
    eka_ind = valinnat[0][0] + valinnat[0][1] * 10
    toka_ind = valinnat[1][0] + valinnat[1][1] * 10
    return eka_ind, toka_ind

def main():     
    klikkaus_nro = 1
    valinnat =[]
    

    while True:       
        naytto.fill((155, 95, 155))   # LILA        

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()                
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                x = tapahtuma.pos[0]
                y = tapahtuma.pos[1]
                valinnat.append(mika_kuva(x, y))   # kuvan indeksi x = 0-9 , y = 0-7
                piirra(valinnat)      
                klikkaus_nro += 1
                if klikkaus_nro == 3:
                   klikkaus_nro = 1 
                   eka, toka = tutki_valinnat(valinnat)  # kuva 0-69
                   if kuvat[eka] == kuvat[toka]:
                       pois_pelista.append(valinnat)
                   valinnat =[]
                   print(pois_pelista)
                   for item in pois_pelista:
                        print((0,0) in item)

                
                
        pygame.display.flip() 
        #pygame.time.delay(2500)  
        kello.tick(100)   
        # END WHILE

            
    
                        

 # # # # # #     MAIN     # # # # # # # # # #

pygame.init()
WIDTH = 990
HEIGHT = 880
VALI_X = 100
VALI_Y = 128

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

kuvat = []
taka = pygame.image.load("kortin_takapuoli.png")
taka = pygame.transform.scale(taka, (90, 111) )
pois_pelista = []

lataa_kuvat()     
main()