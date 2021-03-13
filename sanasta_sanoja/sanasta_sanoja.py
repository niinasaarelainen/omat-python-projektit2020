import pygame, random



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
        sanat_8 = ["MANSIKKA", "MUSTIKKA", "PENSSELI"]
        return sanat_8       
        

    def arvo_sana(self):         
        r = random.randint(0, len(self.sanat) -1)
        return self.sanat[r]

            

def sanat_nakyviin(rivi_keskenerainen, rivit_ruudulla, arvottu_sana):
    
    # arvottu sana:
    t = fontti_iso.render(arvottu_sana, True, musta)
    naytto.blit(t, (200, 20))

    # vanhat rivit:
    y = 77
    for sana in rivit_ruudulla:
        s = ""
        s = s.join(sana) 
        t = fontti_keski.render(s, True, vari)
        naytto.blit(t, (50, y))
        y += 40

    # keskeneräinen, uusin rivi:
    s = ""
    s = s.join(rivi_keskenerainen) 
    t = fontti_keski.render(s, True, vari)
    naytto.blit(t, (50, y))


def pisteet_nakyviin(pisteet):
    t = fontti_keski.render(f"{pisteet}", True, musta)
    naytto.blit(t, (WIDTH - 50, 20))



def main():
    pisteet = 0 
    sana = []
    rivi = []
    sanat = []
    rivit_ruudulla = []
    y = 60
    arvottu_sana = sanastaSanoja.arvo_sana()

    while True:
        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN:    
                    # välilyönti tai ENTER = sananvaihto               
                    if tapahtuma.key == pygame.K_SPACE or tapahtuma.key == pygame.K_RETURN:
                        pisteet += 1  
                        rivi.append(chr(tapahtuma.key))
                        print(rivit_ruudulla)  
                        sanat.append(sana)  
                        sana = []
                        if len(rivi) > 40:
                            rivit_ruudulla.append(rivi)
                            rivi = []  
                    else:
                        rivi.append(chr(tapahtuma.key))
            
        naytto.fill(valkoinen)
        sanat_nakyviin(rivi, rivit_ruudulla, arvottu_sana)     
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
main()