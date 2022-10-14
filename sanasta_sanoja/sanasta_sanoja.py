import pygame, random 
from itertools import permutations

# CTRL + F5  !!!!!!!!!!

#################################################################################################
class LoydaKaikki():
    def __init__(self, lista, sana):        
        self.sanalista = lista
        self.sana_orig = sana.lower()
        self.sana = list(sana.lower())        
        self.kokelaat = []
        self.uniikit = []           # kirjainyhdistelmät
        self.loydetyt_sanat = []    # hyväksytyt engl.sanat
    
    def permutoi_sana(self, sana):
        perms = [''.join(p) for p in permutations(sana)]
        return perms

    def test_sets(self):
        s1 =  set(["a", "b"])
        s2 =  set(["b", "a"])
        s3 =  set(["a", "a", "b"])   # kaikista tulee {'b', 'a'}
        print(s1, s2, s3)
        print(s1 == s3)    # True !!!!!!!!!!!!!!!!!!!   eli setit ei toimikaan ---> ei löydy sana bomb

    def sub_lists (self): 
        base = []   
        lists = [base] 
        for i in range(len(self.sana)): 
            orig = lists[:] 
            new = self.sana[i] 
            for j in range(len(lists)): 
                lists[j] = lists[j] + [new] 
            lists = orig + lists 
        self.kokelaat = lists        
        return lists 

    def lists_to_uniikit(self):
        for sana in self.kokelaat:
            if sorted(sana) not in self.uniikit:
                self.uniikit.append(sorted(sana))

    def etsi(self):  
        self.sub_lists() 
        self.lists_to_uniikit()  
        print("self.uniikit", sorted(self.uniikit))   
        for sana in self.uniikit:
            permutoidut = self.permutoi_sana(sana)
            for perm in permutoidut:
                if perm in self.sanalista and perm not in self.loydetyt_sanat and perm != self.sana_orig:
                    self.loydetyt_sanat.append(perm) 


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
        
        sanat_8_eng = ["ATOMBOMB", "MONOPOLY"]    # 8kirj. = 40320 permutaatiota  (+2-7kirj)
        löytyy_failista = ["STUDIOS", "VISUAL", "MATINEE", "RABBITS", "GIANTS"]  
        löytyy_failista = ["MANSIKKA", "MUSTIKKA", "PENSSELI", "HARAKIRI", "ELOHIIRI"]   
        return löytyy_failista
        

    def arvo_sana(self):         
        r = random.randint(0, len(self.sanat) -1)
        return self.sanat[r]

#################################################################################################

def open_files():
    f = open("aiemmin_keksityt.txt", "r")   # 3 eri failia
    rivit= []
    for rivi in f:    
        rivit.append(rivi)  
    with open("wordlist.txt") as tiedosto:   # .strip()  olisi kannattanut laittaa AINA !!!!   MUISTA !!!!!
        rivit2= []
        for rivi in tiedosto:    
            rivit2.append(rivi.strip()) 
    with open("wordlistasta_loytyvat.txt") as tiedosto:
        rivit3= []
        for rivi in tiedosto:    
            rivit3.append(rivi.strip())  # ensin lista
        # sitten sanakirja:
        sanakirja= {}
        for rivi_nro in range(0, len(rivit3), 2):  
            sanakirja[rivit3[rivi_nro]] = rivit3[rivi_nro + 1]
    return rivit, rivit2, sanakirja


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
    with open("aiemmin_keksityt.txt", "w") as tiedosto:
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


def muut_tekstit_nakyviin(pisteet):
    global error_msg
    t = fontti_keski.render(f"{pisteet}/{maksimi}", True, musta)
    naytto.blit(t, (WIDTH - 130, 20))
    t = fontti_pieni_bold.render(f"F9 = tallenna sanat & uusi sana", True, musta)
    naytto.blit(t, (WIDTH - 260, HEIGHT - 30))
    t = fontti_pieni_bold.render(f"{error_msg}", True, musta)
    naytto.blit(t, (20, HEIGHT - 30))


def onko_laillinen(arvottu_sana, sana):
    global error_msg
    s = ""
    s = s.join(sana) 
    if s.upper() == arvottu_sana:
        error_msg = "Ei koko sanaa sellaisenaan"
        return False    
    arvottu_sana_list= list(arvottu_sana)
    for kirjain in sana:
        if kirjain.upper() in arvottu_sana_list:
            arvottu_sana_list.remove(kirjain.upper())
        else:
            error_msg = f"{arvottu_sana} Ei tuota yrittämääsi sanaa"
            return False
    if f"{s}" not in wordlist:
        error_msg = "Ei ole englannin sana"
        return False
    if s in sanat:
        error_msg = "Tämä sana on jo keksitty"
        return False
    error_msg = ""
    return True
    

def main():
    global sanat, arvottu_sana, aiemmin_keksityt, maksimi
    pisteet = len(sanat) 
    keskenerainen_sana = []
    pelataan = True

    while pelataan:
        naytto.fill(valkoinen)
        sanat_nakyviin(sanat, arvottu_sana, keskenerainen_sana)     
        muut_tekstit_nakyviin(pisteet)   

        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN: 

                    # keksimisen lopetus F9 & uusi sana
                    if tapahtuma.key == pygame.K_F9:
                        sana = ""
                        sana = sana.join(keskenerainen_sana)
                        if len(keskenerainen_sana) > 0 and onko_laillinen(arvottu_sana, keskenerainen_sana):
                            pisteet += 1  
                            sanat.append(sana)    
                        print("sanat", sanat)                      
                        write_file(sanat, arvottu_sana, aiemmin_keksityt)
                        aiemmin_keksityt, file2, file3 = open_files()
                        arvottu_sana_uusi = sanastaSanoja.arvo_sana()
                        while arvottu_sana_uusi == arvottu_sana:
                            arvottu_sana_uusi = sanastaSanoja.arvo_sana()
                        arvottu_sana = arvottu_sana_uusi                        
                        kaikki_mahdolliset_sanat_tasta_sanasta = wordlistasta_loytyvat[arvottu_sana]
                        maksimi = kaikki_mahdolliset_sanat_tasta_sanasta.count(',') + 1
                        sanat = scan_file(aiemmin_keksityt, arvottu_sana)
                        pisteet = len(sanat) 
                        keskenerainen_sana = []

                    # välilyönti  tai ENTER :        
                    elif tapahtuma.key == pygame.K_SPACE or tapahtuma.key == pygame.K_RETURN:
                        sana = ""
                        sana = sana.join(keskenerainen_sana)
                        if len(keskenerainen_sana) > 0 and onko_laillinen(arvottu_sana, keskenerainen_sana):
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
musta = (3, 3, 3)                                   # CTRL + F5  !!!!!!!!!!
punainen = (255, 0, 0)
error_msg = ""


arvottu_sana= sanastaSanoja.arvo_sana()             
aiemmin_keksityt, wordlist, wordlistasta_loytyvat = open_files()
kaikki_mahdolliset_sanat_tasta_sanasta = wordlistasta_loytyvat[arvottu_sana]    # huom! string joka näyttää listalta !!
print(kaikki_mahdolliset_sanat_tasta_sanasta)
maksimi = kaikki_mahdolliset_sanat_tasta_sanasta.count(',') + 1
kaikki = LoydaKaikki(wordlist, arvottu_sana)

"""
kaikki.etsi()
print(sorted(kaikki.uniikit))
print(sorted(kaikki.loydetyt_sanat))
print(len(kaikki.loydetyt_sanat))   """ 

sanat = scan_file(aiemmin_keksityt, arvottu_sana)
main()