data = []
winning = []
omat_numerot = []
montako_oikein = {}
scratchcards = 0
instances_of_cards = {}

def readfile():
    f = open("data_1.txt", "r") 
    for rivi in f:
        alku, loppu = rivi.strip().split(": ")   # alku turha
        data.append(loppu.strip().split(" | "))  


def teeTietorakenteet():  
    global winning, omat_numerot
    for rivi in data:
        win = rivi[0].replace("  ", " ").split(" ")
        omat = rivi[1].replace("  ", " ").split(" ")
        winning.append(win)
        omat_numerot.append(omat)

def montakoOikein_apu(uudet_kortit): 
    print("uudet_kortit alussa", uudet_kortit)
    global scratchcards 
    for card in uudet_kortit:
        scratchcards += montako_oikein[card]
        instances_of_cards[card] += 1        
        uudet_kortit = [i+card + 1 for i in range(montako_oikein[card])]  
        for card in uudet_kortit:
            scratchcards += montako_oikein[card]
            instances_of_cards[card] += 1   
            uudet_kortit = [i+card + 1 for i in range(montako_oikein[card])]  
            for card in uudet_kortit:
                scratchcards += montako_oikein[card]
                instances_of_cards[card] += 1   
                uudet_kortit = [i+card + 1 for i in range(montako_oikein[card])]  
                for card in uudet_kortit:
                    scratchcards += montako_oikein[card]
                    instances_of_cards[card] += 1   
                    uudet_kortit = [i+card + 1 for i in range(montako_oikein[card])]  
                    for card in uudet_kortit:
                        scratchcards += montako_oikein[card]
                        instances_of_cards[card] += 1   
        

def montakoOikein():
    global montako_oikein
    for ind in range(len(data)):
        oikein = 0
        
        for nro in winning[ind]:
            if nro in omat_numerot[ind]:
                oikein += 1

        montako_oikein[ind + 1] =  oikein 
        instances_of_cards[ind + 1] = 1
        

def kayLapi():
    global montako_oikein
    for ind in range(len(montako_oikein)):
        print("Card"+str(ind +1))
        print(instances_of_cards)
        uudet_kortit = [i+ind + 2 for i in range(montako_oikein[ind + 1])]        
        montakoOikein_apu(uudet_kortit)


readfile()
teeTietorakenteet()
montakoOikein()

kayLapi()
print(instances_of_cards)


#print(kerroKahdella(12-1))
#print(kerroKahdella(10-1))   # 512 pitäisi olla max !!!
#print(kerroKahdella(5-1))
