import pygame
from vakiot import *


def gameover(pisteet, naytto):
    naytto.fill(ruskea)
    hiscore(pisteet)
    pygame.display.update()
    pygame.time.delay(500)  # 1/2 sekunnin viive, jottei käyttäjän edellinen peli käynnistä tahattomasti uutta
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:  # palaa main():iin
                return
           elif event.type == pygame.QUIT:
               pygame.quit()
               

def hiscore(pisteet):
    f = open("hiscore.txt", "r")
    fontti_iso = pygame.font.SysFont("Arial", 36)
    fontti_pieni_bold = pygame.font.SysFont("Arial", 24, bold = True)
    uudestaan = fontti_pieni_bold.render("uusi peli: mikä tahansa näppäin", 1, vihrea)   # uusi peli
    naytto.blit(uudestaan, (200 , HEIGHT - 160))

    top5 = [int(rivi.replace("\n", "")) for rivi in f]       

    if pisteet < top5[-1]:        
        top5.append(pisteet)        
        top5 = sorted(top5)
        #top5.reverse()
        monesko = top5.index(pisteet) + 1
        monesko_str = {1:"paras !!!", 2:"toka !!", 3:"kolmas !", 4:"neljäs", 5:"viides"}
        text = fontti_iso.render(f"Olet {monesko_str[monesko]}", 1, vihrea)
    else:
        text = fontti_iso.render("Ei riitä Top5:een:", 1, vihrea)
    naytto.blit(text, (150, 60))

    y = 140    
    for rivi in top5[:5]:
        luku = fontti_iso.render(str(rivi), 1, vihrea)
        naytto.blit(luku, (200, y))
        y += 40
        
    write_file(top5[:5])
    

def write_file(lista):
    with open("hiscore.txt", "w") as tiedosto:
        for rivi in lista:
            tiedosto.write(str(rivi)+"\n")


