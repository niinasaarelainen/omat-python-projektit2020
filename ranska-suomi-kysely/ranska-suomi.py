import pygame, random 

# CTRL + F5  !!!!!!!!!!


def open_file():

    f = open("mots.txt", "r")  
    rivit= []
    for rivi in f:          
        rivit.append(rivi.strip())  

    d = {}
    for i in range(len(rivit) - 1):
        if  i % 2 == 0: 
            d[rivit[i]] = rivit[i + 1]
    return d


def muut_tekstit_nakyviin(pisteet, maksimi):
    t = fontti_keski.render(f"{pisteet}/{maksimi}", True, vihrea)
    naytto.blit(t, (WIDTH - 90, 20))

def arvo():
    print(len(dict))
    lista = list(dict)
    l2 = []
    vastaus = []
    arvottu_sana = random.choice(lista) 
    vastaus.append(arvottu_sana)  
    oikea_vastaus = dict[arvottu_sana]  
    l2.append(arvottu_sana)
    l2.append(oikea_vastaus)
    kaikki_suomeksi.remove(oikea_vastaus)  

    vaara1 = random.choice(kaikki_suomeksi)  
    l2.append(vaara1)
    kaikki_suomeksi.remove(vaara1)  

    vaara2 = random.choice(kaikki_suomeksi)  
    l2.append(vaara2)
    kaikki_suomeksi.append(vaara1)
    kaikki_suomeksi.append(oikea_vastaus)

    for sana in l2:
        for muunnos in muunnokset:
            if muunnos in sana:                
                sana = sana.replace(muunnos, muunnokset[muunnos])       
        vastaus.append(sana)
    
    return vastaus


def sanat_nakyviin(arvottu_sana, vaihtoehdot ) :
    t = fontti_iso.render(f"{arvottu_sana}", True, musta)
    naytto.blit(t, (110, 45))
    
    t = fontti_keski.render(f"1) {vaihtoehdot[0]}", True, musta)
    naytto.blit(t, (130, 90))
    t = fontti_keski.render(f"2) {vaihtoehdot[1]}", True, musta)
    naytto.blit(t, (130, 120))
    t = fontti_keski.render(f"3) {vaihtoehdot[2]}", True, musta)
    naytto.blit(t, (130, 150))

def lopetusko():
    if len(dict) == 0:
        naytto.fill(valkoinen)
        t = fontti_iso.render(f"Kaikki sanat kyselty. ", True, musta)
        naytto.blit(t, (90, 45))
        t = fontti_iso.render(f"Uusi kierros alkaa 2 s kuluttua", True, musta)
        naytto.blit(t, (90, 85))
        pygame.display.flip()
        pygame.time.delay(2100)
        main()


def main():
    global dict     
    pisteet = 0
    arvaus = 0    
    dict = open_file()
    maksimi = len(dict)
    arvottu_sana_orig, arvottu_sana, oikea_vastaus, vaara1, vaara2 = arvo()
    vaihtoehdot = [oikea_vastaus, vaara1, vaara2]
    random.shuffle(vaihtoehdot)
    oikein = None

    while len(dict) > 0:
        naytto.fill(valkoinen)
        sanat_nakyviin(arvottu_sana, vaihtoehdot )        
        muut_tekstit_nakyviin(pisteet, maksimi)   

        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN: 
    
                    if tapahtuma.key == pygame.K_1:
                        arvaus = 1
                        if oikea_vastaus == vaihtoehdot[arvaus - 1]:
                            pisteet += 1
                            dict.pop(arvottu_sana_orig)
                            lopetusko()
                            oikein = True 
                        else:
                            oikein = False  
                        arvottu_sana_orig, arvottu_sana, oikea_vastaus, vaara1, vaara2 = arvo()
                        vaihtoehdot = [oikea_vastaus, vaara1, vaara2]
                        random.shuffle(vaihtoehdot)        
                    elif tapahtuma.key == pygame.K_2:
                        arvaus = 2
                        if oikea_vastaus == vaihtoehdot[arvaus - 1]:
                            pisteet += 1
                            dict.pop(arvottu_sana_orig)
                            lopetusko()
                            oikein = True 
                        else:
                            oikein = False  
                        arvottu_sana_orig, arvottu_sana, oikea_vastaus, vaara1, vaara2 = arvo()
                        vaihtoehdot = [oikea_vastaus, vaara1, vaara2]
                        random.shuffle(vaihtoehdot)
                    elif tapahtuma.key == pygame.K_3:
                        arvaus = 3
                        if oikea_vastaus == vaihtoehdot[arvaus - 1]:
                            pisteet += 1
                            dict.pop(arvottu_sana_orig)
                            lopetusko()
                            oikein = True 
                        else:
                            oikein = False  
                        arvottu_sana_orig, arvottu_sana, oikea_vastaus, vaara1, vaara2 = arvo()
                        vaihtoehdot = [oikea_vastaus, vaara1, vaara2]
                        random.shuffle(vaihtoehdot)
                        
        
        if oikein:
            naytto.blit(up, (130, 190))            
        elif oikein == False:
            naytto.blit(down, (130, 190))        
        pygame.display.flip()
        kello.tick(400)



pygame.init()
pygame.display.set_caption("Suomi - ranska")
WIDTH = 660
HEIGHT = 400
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

fontti_iso = pygame.font.SysFont("Arial", 36, bold = True)
fontti_keski = pygame.font.SysFont("Arial", 26)
fontti_pieni_bold = pygame.font.SysFont("Arial", 16, bold = True)

valkoinen = (255, 255, 255)
musta = (3, 3, 3)                                   # CTRL + F5  !!!!!!!!!!
punainen = (255, 0, 0)
vihrea = (22, 200, 22)
vari  = valkoinen
error_msg = ""

muunnokset = {"Ã¤": "ä", "Ã\xa0": "à", "Ã©": "é", "Ã¶": "ö", "Ã¢": "á", "Ãª":"ê", "Ã§": "ç", "Ã¨": "è", "Ã´": "ô"}
up = pygame.image.load('up.png')
down = pygame.image.load('down.png')

dict = open_file()
kaikki_suomeksi = list(dict.values())
print(kaikki_suomeksi)
main()