import pygame
from yhteiset import *


def gameover(pisteet, fontti_iso, fontti_pieni):
    hiscore(pisteet, fontti_iso, fontti_pieni)
    pygame.display.update()
    pygame.time.delay(1000)  # sekunnin viive, jottei käyttäjän edellinen peli käynnistä tahattomasti uutta
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:   
                return
           elif event.type == pygame.QUIT:
               pygame.quit()
               

def hiscore(pisteet, fontti_iso, fontti_pieni):
    f = open("hiscore_nuotti.txt", "r")
    uudestaan = fontti_pieni.render("uusi peli: mikä tahansa näppäin", 1, musta)   # uusi peli
    naytto.blit(uudestaan, (433, HEIGHT - 60))

    top5 = []    
    for rivi in f:
        top5.append(int(rivi.replace("\n", "")))

    if pisteet > top5[-1]:        
        top5.append(pisteet)        
        top5 = sorted(top5)
        top5.reverse()
        monesko = top5.index(pisteet) + 1
        monesko_str = {1:"paras !!!", 2:"toka !!", 3:"kolmas !", 4:"neljäs", 5:"viides"}
        text = fontti_iso.render(f"Olet {monesko_str[monesko]}", 1, (220, 10, 10))
    else:
        text = fontti_iso.render("Ei riitä Top5:een:", 1, (220, 10, 10))
    naytto.blit(text, (230, 60))

    y = 140    
    for rivi in top5[:5]:
        luku = fontti_iso.render(str(rivi), 1, (210, 10, 10))
        naytto.blit(luku, (270, y))
        y += 40
        
    write_file(top5[:5])
    

def write_file(lista):
    with open("hiscore_nuotti.txt", "w") as tiedosto:
        for rivi in lista:
            tiedosto.write(str(rivi)+"\n")


