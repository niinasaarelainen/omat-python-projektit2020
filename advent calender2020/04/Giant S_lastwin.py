import sys

data = []
voittonumerot = []   # stringejä !!!                väärä tulos : 2744
bingo_kentat = []
viimeisin_arvottu = 0
voittonumerot_lkm = 0

def readfile():
    global voittonumerot, bingo_kentat, voittonumerot_lkm
    f = open("data.txt", "r") 
    i = 0
    for rivi in f:
        if i == 0:
            voittonumerot.append(rivi.strip().split(","))
            voittonumerot = voittonumerot[0]
            voittonumerot_lkm = len(voittonumerot)
        else:
            if rivi.strip() == '':
               bingo_kentat.append([]) 
            else:
                bingo_kentat[-1].append(rivi.strip().replace("  ", " "))
        i += 1


def loytyyko_numero():
        global viimeisin_arvottu, voittonumerot_lkm  
        summa = 0
        for i in range(voittonumerot_lkm):         
            if len(voittonumerot) > 0:
                viimeisin_arvottu = voittonumerot.pop(0).strip()
            print("viimeisin_arvottu", viimeisin_arvottu)
            for kentta in range(len(bingo_kentat)):
                for rivi in range(len(bingo_kentat[kentta])):  
                    #print("rivi", bingo_kentat[kentta][rivi]) 
                    yksittaiset_numerot = bingo_kentat[kentta][rivi].split(" ")                    
                    for nro in range(len(yksittaiset_numerot)):  
                        if viimeisin_arvottu == yksittaiset_numerot[nro].strip():  
                            yksittaiset_numerot[nro] = "*"                            
                            uusi_rivi = ' '.join(yksittaiset_numerot)
                            bingo_kentat[kentta][rivi] = uusi_rivi
                            #bingo_kentat[kentta][rivi] = bingo_kentat[kentta][rivi].replace(viimeisin_arvottu, "*")               
            voittokentat = voittoko()
            voittokentat.sort(reverse = True)
            print("voittokentat", voittokentat)        
            for kentta in voittokentat:
                print("     poistettiin kenttä", bingo_kentat[kentta])
                summa = laske_summa(kentta)
                bingo_kentat.remove(bingo_kentat[kentta])
                if len(bingo_kentat) == 0:
                    print(" V I K A   ", summa * int(viimeisin_arvottu))
                    sys.exit()  
            #print("len(bingo_kentat)", len(bingo_kentat))              

        
            
                
def voittoko():    
    voittokentat = []
    #vaakatarkistus:
    for kentta in range(len(bingo_kentat)):
        for rivi in range(len(bingo_kentat[kentta])):
            if bingo_kentat[kentta][rivi].count('*') == 5:
                #print("vaakatykki")
                if kentta not in voittokentat:
                    voittokentat.append(kentta)            

    # pystytarkistus
    for kentta in range(len(bingo_kentat)):
        pystyrivi =  []
        for ind in range(len(bingo_kentat[kentta])):
            for rivi in range(len(bingo_kentat[kentta])):
                splitted = bingo_kentat[kentta][rivi].split(" ")
                pystyrivi.append(splitted[ind])
            if pystyrivi.count('*') == 5:   
                #print("pystytykki")
                if kentta not in voittokentat:
                    voittokentat.append(kentta)         
            pystyrivi =  []
    return voittokentat

def laske_summa(kentta):
    print(bingo_kentat[kentta])
    unmarked_numbers = 0
    for rivi in range(len(bingo_kentat[kentta])):
        splitted = bingo_kentat[kentta][rivi].split(" ")
        for nro in splitted:
            if "*" not in nro.strip() and nro.strip() != "":
                unmarked_numbers += int(nro.strip())
    print("unmarked_numbers:", unmarked_numbers)
    return unmarked_numbers


readfile()
loytyyko_numero()
