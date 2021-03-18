import pygame, random


#################################################################################################
class SanastaSanoja:
    
    def __init__(self):        
        self.sanat = self.sanavarasto()
    
    def arvo_vari(self):
        r = random.randint(40, 170)   #ei yli 170, jottei tule liian vaaleaa
        g = random.randint(40, 170)
        b = random.randint(40, 170)
        return r, g, b
    
    def sanavarasto(self):             
        sanat_7 = ["MAALARI", "HAALARI", "HAITARI", "VADELMA"]
        sanat_8 = ["MANSIKKA", "MUSTIKKA", "PENSSELI", "HARAKIRI", "ELOHIIRI"]
        sanat_8_eng = ["ATOM BOMB", "MONOPOLY"]                                         
        return sanat_8_eng       
        

    def arvo_sana(self):         
        r = random.randint(0, len(self.sanat) -1)
        return self.sanat[r]

#################################################################################################

def open_files():
    f = open("sanat_tiedostossa.txt", "r")
    rivit= []
    for rivi in f:    
        rivit.append(rivi)   
    with open("wordlist.txt") as tiedosto:
        rivit2= []
        for rivi in tiedosto:    
            rivit2.append(rivi)   
    return rivit, rivit2

def scan_file(rivit, arvottu_sana):
    muistiin = []
    tallenna = False
    for rivi in rivit:
        if tallenna and "SEURAAVA SANA:" in rivi:
           break
        if tallenna:
            muistiin.append(rivi.strip())
        if arvottu_sana in rivi:
            tallenna = True
    return muistiin
    

def write_file(sanat, arvottu_sana, rivit):
    print("rivit@write_file", rivit, "sanat", sanat)
    
    with open("sanat_tiedostossa.txt", "w") as tiedosto:
        #ensin uusin data:
        tiedosto.write(arvottu_sana + "\n")
        for sana in sanat:
            s = ""
            s = s.join(sana) 
            tiedosto.write(s+"\n")
        tiedosto.write("SEURAAVA SANA:"+"\n")

        #sitten vanha, josta otetaan pois nykyinen sana
        kirjoita_vanhaa_tiedostoa = True    
        for rivi in rivit: # tiedostossa jo olleet kaikki rivit            
            if arvottu_sana in rivi:
                kirjoita_vanhaa_tiedostoa = False
            if kirjoita_vanhaa_tiedostoa:
                tiedosto.write(rivi)
            if "SEURAAVA SANA:" in rivi:
                kirjoita_vanhaa_tiedostoa = True

            

def sanat_nakyviin(sanat, arvottu_sana, keskenerainen_sana):
    
    # arvottu sana:
    t = fontti_iso.render(arvottu_sana, True, musta)
    naytto.blit(t, (200, 20))

    # sanat failista, jos on:
    x = 50    
    y = 77
    for sana in sanat:
        s = ""
        s = s.join(sana) 
        t = fontti_keski.render(s, True, vari)
        naytto.blit(t, (x, y))
        x += len(sana) * 20
        if x > WIDTH - 120:
            x = 50
            y += 40

    # keskeneräinen, uusin rivi:
    s = ""
    s = s.join(keskenerainen_sana) 
    t = fontti_keski.render(s, True, vari)
    naytto.blit(t, (x, y)) 


def pisteet_nakyviin(pisteet):
    t = fontti_keski.render(f"{pisteet}", True, musta)
    naytto.blit(t, (WIDTH - 50, 20))
    t = fontti_pieni_bold.render(f"F9 = tallenna sanat & uusi sana", True, musta)
    naytto.blit(t, (WIDTH - 260, HEIGHT - 30))


def onko_laillinen(arvottu_sana, sana):
    s = ""
    s = s.join(sana) 
    if s.upper() == arvottu_sana:
        return False
    print(f"{s}\n")
    if f"{s}\n" not in wordlist:
        return False
    arvottu_sana= list(arvottu_sana)
    for kirjain in sana:
        if kirjain.upper() in arvottu_sana:
            arvottu_sana.remove(kirjain.upper())
        else:
            return False
    return True





def main():
    global sanat, arvottu_sana, file
    pisteet = len(sanat) 
    keskenerainen_sana = []
    pelataan = True

    while pelataan:
        naytto.fill(valkoinen)
        sanat_nakyviin(sanat, arvottu_sana, keskenerainen_sana)     
        pisteet_nakyviin(pisteet)   

        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN: 

                    # keksimisen lopetus F9 & uusi sana
                    if tapahtuma.key == pygame.K_F9:
                        sana = ""
                        sana = sana.join(keskenerainen_sana)
                        if len(keskenerainen_sana) > 0 and not sana in sanat and onko_laillinen(arvottu_sana, keskenerainen_sana):
                            pisteet += 1  
                            sanat.append(sana)                          
                        write_file(sanat, arvottu_sana, file)
                        file, file2 = open_files()
                        arvottu_sana_uusi = sanastaSanoja.arvo_sana()
                        while arvottu_sana_uusi == arvottu_sana:
                            arvottu_sana_uusi = sanastaSanoja.arvo_sana()
                        arvottu_sana = arvottu_sana_uusi
                        sanat = scan_file(file, arvottu_sana)
                        pisteet = len(sanat) 
                        keskenerainen_sana = []

                    # välilyönti  tai ENTER :        
                    elif tapahtuma.key == pygame.K_SPACE or tapahtuma.key == pygame.K_RETURN:
                        sana = ""
                        sana = sana.join(keskenerainen_sana)
                        if len(keskenerainen_sana) > 0 and not sana in sanat and onko_laillinen(arvottu_sana, keskenerainen_sana):
                            pisteet += 1  
                            sanat.append(sana)                        
                        keskenerainen_sana= []

                    # backspace:
                    elif tapahtuma.key == pygame.K_BACKSPACE:
                        keskenerainen_sana.pop(-1)
                    else:
                        keskenerainen_sana.append(chr(tapahtuma.key))

            
        

        pygame.display.flip()
        kello.tick(100)



pygame.init()
pygame.display.set_caption("Muodosta uusia sanoja sanasta...")
WIDTH = 660
HEIGHT = 400
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

fontti_iso = pygame.font.SysFont("FreeMono", 36, bold = True)
fontti_keski = pygame.font.SysFont("FreeMono", 26)
fontti_pieni_bold = pygame.font.SysFont("Arial", 16, bold = True)

sanastaSanoja = SanastaSanoja()
vari = sanastaSanoja.arvo_vari()
valkoinen = (255, 255, 255)
musta = (3, 3, 3)
punainen = (255, 0, 0)

arvottu_sana= sanastaSanoja.arvo_sana()
file, wordlist = open_files()
print("file:", file)
sanat = scan_file(file, arvottu_sana)
print("sanat:", sanat)
main()