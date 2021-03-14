import pygame, random


#################################################################################################
class SanastaSanoja:
    
    def __init__(self):        
        self.sanat = self.sanavarasto()
    
    def arvo_vari(self):
        r = random.randint(30, 200)   #ei yli 200, jottei tule liian vaaleaa
        g = random.randint(30, 200)
        b = random.randint(30, 200)
        return r, g, b
    
    def sanavarasto(self):             
        sanat_7 = ["MAALARI", "HAALARI", "HAITARI", "VADELMA"]
        # sanat_8 = ["MANSIKKA", "MUSTIKKA", "PENSSELI"]
        sanat_8 = ["MANSIKKA"]                                           # TEST TODO vaihda
        return sanat_8       
        

    def arvo_sana(self):         
        r = random.randint(0, len(self.sanat) -1)
        return self.sanat[r]

#################################################################################################

def open_file():
    f = open("sanat_tiedostossa.txt", "r")
    rivit= []
    for rivi in f:    
        rivit.append(rivi)     
    return rivit

def scan_file(rivit, arvottu_sana):
    muistiin = []
    tallenna = False
    for rivi in rivit:
        if "SEURAAVA SANA:" in rivi:
           break
        if tallenna:
            muistiin.append(rivi.strip())
            print("rivi@tallenna:", rivi)
        if arvottu_sana in rivi:
            tallenna = True
    return muistiin
    

def write_file(sanat, arvottu_sana):
    with open("sanat_tiedostossa.txt", "w") as tiedosto:
        tiedosto.write(arvottu_sana+"\n")
        for rivi in sanat:
            s = ""
            s = s.join(rivi) 
            tiedosto.write(s+"\n")
        tiedosto.write("SEURAAVA SANA:")
            

def sanat_nakyviin(sanat, rivi_keskenerainen, rivit_ruudulla, arvottu_sana):
    
    # arvottu sana:
    t = fontti_iso.render(arvottu_sana, True, musta)
    naytto.blit(t, (200, 20))

    # sanat failista, jos on:
    x = 50    
    y = 77
    for sana in sanat:
        print("sana rivi 70", sana)
        t = fontti_keski.render(sana, True, vari)
        naytto.blit(t, (x, y))
        x += len(sana) * 14
        if x > WIDTH - 100:
            x = 50
            y += 40

    # tämän pelikerran sanat:
    for sana in rivit_ruudulla:
        s = ""
        s = s.join(sana) 
        t = fontti_keski.render(s, True, vari)
        naytto.blit(t, (x, y))
        y += 40

    # keskeneräinen, uusin rivi:
    s = ""
    s = s.join(rivi_keskenerainen) 
    t = fontti_keski.render(s, True, vari)
    naytto.blit(t, (x, y))


def pisteet_nakyviin(pisteet):
    t = fontti_keski.render(f"{pisteet}", True, musta)
    naytto.blit(t, (WIDTH - 50, 20))
    t = fontti_pieni_bold.render(f"F9 = en keksi enempää sanoja", True, musta)
    naytto.blit(t, (WIDTH - 240, HEIGHT - 30))


def onko_laillinen(arvottu_sana, sana):
    s = ""
    s = s.join(sana) 
    if s.upper() == arvottu_sana:
        return False
    arvottu_sana = list(arvottu_sana)
    for kirjain in sana:
        if kirjain.upper() in arvottu_sana:
            arvottu_sana.remove(kirjain.upper())
        else:
            return False
    return True


def main():
    global sanat
    pisteet = 0 
    sana = []
    rivi = []
    rivit_ruudulla = []
    y = 60
    pelataan = True

    while pelataan:
        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN: 

                    # keksimisen lopetus F9
                    if tapahtuma.key == pygame.K_F9:
                        pelataan = False 
                        rivit_ruudulla.append(rivi)
                        if len(sana) > 0 and not sana in sanat and onko_laillinen(arvottu_sana, sana):
                            pisteet += 1  
                            sanat.append(sana)  

                    # välilyönti  tai ENTER :        
                    elif tapahtuma.key == pygame.K_SPACE or tapahtuma.key == pygame.K_RETURN:
                        if len(sana) > 0 and not sana in sanat and onko_laillinen(arvottu_sana, sana):
                            pisteet += 1  
                            sanat.append(sana)  
                        rivi.append(chr(pygame.K_SPACE))                        
                        sana = []
                        if len(rivi) > 40:
                            rivit_ruudulla.append(rivi)
                            rivi = []  

                    # backspace:
                    elif tapahtuma.key == pygame.K_BACKSPACE:
                        rivi.pop(-1)
                    else:
                        rivi.append(chr(tapahtuma.key))
                        sana.append(chr(tapahtuma.key))

            
        naytto.fill(valkoinen)
        sanat_nakyviin(sanat, rivi, rivit_ruudulla, arvottu_sana)     
        pisteet_nakyviin(pisteet)   

        pygame.display.flip()
        kello.tick(100)



pygame.init()
pygame.display.set_caption("Muodosta uusia sanoja sanasta...")
WIDTH = 660
HEIGHT = 400
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

fontti_iso = pygame.font.SysFont("Arial", 36)
fontti_keski = pygame.font.SysFont("Arial", 26)
fontti_pieni_bold = pygame.font.SysFont("Arial", 16, bold = True)

sanastaSanoja = SanastaSanoja()
vari = sanastaSanoja.arvo_vari()
valkoinen = (255, 255, 255)
musta = (3, 3, 3)
punainen = (255, 0, 0)

arvottu_sana = sanastaSanoja.arvo_sana()
file = open_file()
print("file:", file)
sanat = scan_file(file, arvottu_sana)
print("sanat:", sanat)
main()
write_file(sanat, arvottu_sana)