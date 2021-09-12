import random, pygame
import glob



def alkukysely():
    fontti = pygame.font.SysFont("FreeMono", 38)
    valinta = 0
    
    while True:   
        naytto.fill(LILA)          
        lkm = fontti.render(f"Montako korttia? Paina 1 - 7 ", True, VIHREE)
        naytto.blit(lkm, (78, 46))
        lkm = fontti.render(f"1 = 10,  2 = 20, ...  7 = 70 ", True, VIHREE)
        naytto.blit(lkm, (138, 139))
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()                
            if tapahtuma.type == pygame.KEYDOWN:  
                print(tapahtuma.key)
                if tapahtuma.key < 49:
                    tapahtuma.key = 49   
                if tapahtuma.key > 55:
                    tapahtuma.key = 55             
                return (tapahtuma.key - 48) * 10
        pygame.display.flip() 



def lataa_kuvat(korttien_lkm):
    i = 0
    kuvat_temp = []
    for filename in glob.iglob('t:/python/climbing_olympics_luokat/kiipeilijoiden_kuvat' + '**/*.png', recursive=True):          
        kuva = pygame.image.load(filename)
        kuva = pygame.transform.scale(kuva, (90, 111) )
        kuvat_temp.append(kuva) 
        kuvat_temp.append(kuva)        
        i += 1
    for i in range(korttien_lkm // 2):
        r = random.randint(0, len(kuvat_temp)//2 -1)
        kuvat.append(kuvat_temp[r * 2])
        kuvat.append(kuvat_temp[r * 2 + 1])
    random.shuffle(kuvat)
        

def piirra(valinnat, korttien_lkm): 
    y = 0
    x = 0
    for i in range(korttien_lkm):
        if (x, y) not in pois_pelista:
            naytto.blit(taka, (x * VALI_X, y * VALI_Y))
        x += 1
        if x == 10:
            y += 1
            x = 0    
    for x, y in valinnat:     
        naytto.blit(kuvat[x + y * 10], (x * VALI_X, y * VALI_Y))

def mika_kuva(x, y):
    x_ind = x // VALI_X
    y_ind = y // VALI_Y
    return x_ind, y_ind


def tutki_valinnat(valinnat):  # valinnat = x, y
    vastaus = []
    for i in range(len(valinnat)):
        ind = valinnat[i][0] + valinnat[i][1] * 10
        vastaus.append(ind)
    return vastaus


def main(korttien_lkm):     
    klikkaus_nro = 1
    valinnat =[]   
    siirto = 0

    while len(pois_pelista) < korttien_lkm:       
        naytto.fill(LILA)           

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()                
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                x = tapahtuma.pos[0]
                y = tapahtuma.pos[1]
                if mika_kuva(x, y) not in valinnat:
                    valinnat.append(mika_kuva(x, y))   # kuvan indeksi x = 0-9 , y = 0-7                
                    klikkaus_nro += 1                
                    
                
        piirra(valinnat, korttien_lkm) 
        
        pygame.display.flip() 

        if klikkaus_nro == 3:
            klikkaus_nro = 1 
            siirto += 1 
            pygame.display.set_caption(f"\tsiirtoja: {siirto}")    
            eka, toka = tutki_valinnat(valinnat)  # kuva 0-69
            if kuvat[eka] == kuvat[toka]:
                pois_pelista.append(valinnat[0])
                pois_pelista.append(valinnat[1])
            valinnat = []       
            pygame.time.delay(1700)             
        
        kello.tick(2000)              
    
                        

 # # # # # #     MAIN     # # # # # # # # # #

pygame.init()
WIDTH = 990
HEIGHT = 880
VALI_X = 100
VALI_Y = 128

LILA = (155, 95, 155)
VIHREE =  (13, 223, 23)

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

taka = pygame.image.load("kortin_takapuoli.png")
taka = pygame.transform.scale(taka, (90, 111) )


while True:
    kuvat = []
    pois_pelista = []
    pygame.display.set_caption(f"\tsiirtoja: 0") 
    korttien_lkm = alkukysely()
    lataa_kuvat(korttien_lkm)   
    main(korttien_lkm)