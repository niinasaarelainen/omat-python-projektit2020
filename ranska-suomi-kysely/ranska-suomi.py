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
    t = fontti_keski.render(f"{pisteet}/{maksimi}", True, musta)
    naytto.blit(t, (WIDTH - 90, 20))

def arvo():
    lista = list(dict)
    arvottu_sana = random.choice(lista)    
    oikea_vastaus = dict[arvottu_sana]  
    lista.remove(arvottu_sana)  

    s = random.choice(lista)    
    vaara1 = dict[s]   
    lista.remove(s)  

    s = random.choice(lista)    
    vaara2 = dict[s]  
    lista.remove(s)   
    
    return arvottu_sana, oikea_vastaus, vaara1, vaara2


def sanat_nakyviin(arvottu_sana, vaihtoehdot ) :
    t = fontti_iso.render(f"{arvottu_sana}", True, musta)
    naytto.blit(t, (110, 45))
    
    t = fontti_keski.render(f"1) {vaihtoehdot[0]}", True, musta)
    naytto.blit(t, (130, 90))
    t = fontti_keski.render(f"2) {vaihtoehdot[1]}", True, musta)
    naytto.blit(t, (130, 120))
    t = fontti_keski.render(f"3) {vaihtoehdot[2]}", True, musta)
    naytto.blit(t, (130, 150))

def main():
    maksimi = len(dict) 
    pisteet = 0
    arvaus = 0
    arvottu_sana, oikea_vastaus, vaara1, vaara2 = arvo()
    vaihtoehdot = [oikea_vastaus, vaara1, vaara2]
    random.shuffle(vaihtoehdot)

    while len(dict) > 3:
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
                            dict.pop(arvottu_sana)
                        arvottu_sana, oikea_vastaus, vaara1, vaara2 = arvo()
                        vaihtoehdot = [oikea_vastaus, vaara1, vaara2]
                        random.shuffle(vaihtoehdot)
                    elif tapahtuma.key == pygame.K_2:
                        arvaus = 2
                        if oikea_vastaus == vaihtoehdot[arvaus - 1]:
                            pisteet += 1
                            dict.pop(arvottu_sana)
                        arvottu_sana, oikea_vastaus, vaara1, vaara2 = arvo()
                        vaihtoehdot = [oikea_vastaus, vaara1, vaara2]
                        random.shuffle(vaihtoehdot)
                    elif tapahtuma.key == pygame.K_3:
                        arvaus = 3
                        if oikea_vastaus == vaihtoehdot[arvaus - 1]:
                            pisteet += 1
                            dict.pop(arvottu_sana)
                        arvottu_sana, oikea_vastaus, vaara1, vaara2 = arvo()
                        vaihtoehdot = [oikea_vastaus, vaara1, vaara2]
                        random.shuffle(vaihtoehdot)
        

        pygame.display.flip()
        kello.tick(400)



pygame.init()
pygame.display.set_caption("Suomi - ranska")
WIDTH = 660
HEIGHT = 400
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

fontti_iso = pygame.font.SysFont("FreeMono", 36, bold = True)
fontti_keski = pygame.font.SysFont("FreeMono", 26)
fontti_pieni_bold = pygame.font.SysFont("Arial", 16, bold = True)

valkoinen = (255, 255, 255)
musta = (3, 3, 3)                                   # CTRL + F5  !!!!!!!!!!
punainen = (255, 0, 0)
vari  = valkoinen
error_msg = ""


#arvottu_sana= sanastaSanoja.arvo_sana()   

dict = open_file()
print(dict)
main()