import random, pygame.midi, pygame


def generoi_melodia():
    aanet = "zxcvbn"  # näppäimistön alin rivi 6 ekaa
    return [aanet[random.randint(0,5)]  for i in range(20)]


def midi_play(n, edellinen, instrument):
    midi_out.set_instrument(instrument)  
    midi_numbers = {"z":60, "x":62, "c":64, "v":65, "b":67, "n":69}    #60 = keski-c, 67 = g
    midi_out.note_off(midi_numbers[edellinen], 110)
    midi_out.note_on(midi_numbers[n], 110)


def soita_melodia(melodia, montako):
    edellinen = "z"
    for i in range(montako):
        midi_play(melodia[i], edellinen, 2)
        edellinen = melodia[i]
        pygame.time.delay(400)
        
   

def mainloop():
    montako = 3
    edellinen = "z"
    melodia = generoi_melodia()
    koneen_vuoro = True
    monesko_kayttajan_aani = 0
    pisteet = 0

    while True:
        naytto.fill(10, 10, 10)
        teksti = fontti_keski.render(f"melodian pituus: {montako}", True, (0, 67, 67))  
        naytto.blit(teksti, (25, 25))    
        if koneen_vuoro:
            pygame.time.delay(700)
            soita_melodia(melodia, montako)
            koneen_vuoro = False
            montako += 1
            monesko_kayttajan_aani = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                midi_play(chr(event.key), edellinen, 6)
                edellinen = chr(event.key)
                monesko_kayttajan_aani += 1
                print(montako)
                if monesko_kayttajan_aani == montako -1:
                    koneen_vuoro = True
                    print("koneen_vuoro = True")
       
       
        kello.tick(40)


pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)

kello = pygame.time.Clock()
naytto = pygame.display.set_mode((211, 211))
fontti_keski = pygame.font.SysFont("Arial", 30)    

if __name__ == "__main__":
    
    mainloop()    








