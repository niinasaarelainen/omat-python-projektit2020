import random, pygame.midi, pygame

def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    return [kirjainvalinta(pituus,kirjaimet) for i in range(maara)]


def kirjainvalinta(pituus, kirjaimet):
    return "".join([random.choice(kirjaimet) for i in range(pituus)])

def midi_play(n, instrument):
    midi_out.set_instrument(instrument)  
    midi_numbers = {"c":60, "d":62, "e":64, "f":65, "g":67, "a":69}    #60 = keski-c, 67 = g
    midi_out.note_on(midi_numbers[n], 110)


def generoi_tititaa(sanagen):
    for sana in sanagen:
        midi_play(sana[0], 14)
        for kirjain in sana:
            midi_play(kirjain, 12)            
            kello.tick(6)
        kello.tick(6)

def generoi_2x_taataataa(sanagen, sanagen2):
    sana2 = 0
    kirjain2 = 0
    for sana in sanagen:
        kirjain2 = 0
        for kirjain in sana:
            midi_play(kirjain, 12)                
            midi_play(sanagen2[sana2][kirjain2], 13)        
            kello.tick(3)
            kirjain2 += 1
        sana2 += 1
        

   

pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)


kello = pygame.time.Clock()
    

if __name__ == "__main__":
    sanagen = sanageneraattori("cdefga", 3, 20)  # A-osa
    generoi_tititaa(sanagen)

    sanagen2 = sanageneraattori("cdefga", 3, 20)  # B-osa
    print(sanagen2)
    generoi_2x_taataataa(sanagen, sanagen2)

    sanagen = sanageneraattori("cdefga", 3, 20)     # A-osan variaatio
    generoi_tititaa(sanagen)

    sanagen2 = sanageneraattori("cdefga", 3, 20)   # B-osan variaatio
    print(sanagen2)
    generoi_2x_taataataa(sanagen, sanagen2)

    sanagen = sanageneraattori("cdefga", 3, 20)     # A-osan uusi variaatio 2 kertaa
    generoi_tititaa(sanagen)
    generoi_tititaa(sanagen)











