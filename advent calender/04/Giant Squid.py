import sys

data = []
voittonumerot = []   # stringejä !!!
bingo_kentat = []
viimeisin_arvottu = 0
jatketaan = True

def readfile():
    global voittonumerot, bingo_kentat
    f = open("data_easy2.txt", "r") 
    i = 0
    for rivi in f:
        if i == 0:
            voittonumerot.append(rivi.strip().split(","))
            voittonumerot = voittonumerot[0]
        else:
            if rivi.strip() == '':
               bingo_kentat.append([]) 
            else:
                bingo_kentat[-1].append(rivi.strip().replace("  ", " "))
        i += 1


def loytyyko_numero():
        global viimeisin_arvottu, jatketaan  
        
        for nro in voittonumerot:
            viimeisin_arvottu = voittonumerot.pop(0).strip()
            print(viimeisin_arvottu)
            for kentta in range(len(bingo_kentat)):
                for rivi in range(len(bingo_kentat[kentta])):                
                    if viimeisin_arvottu in bingo_kentat[kentta][rivi].split(" "):  # TODO  1 --> 14 --> * 4  EIIII
                        bingo_kentat[kentta][rivi] = bingo_kentat[kentta][rivi].replace(viimeisin_arvottu, " * ")
                        bingo_kentat[kentta][rivi] = bingo_kentat[kentta][rivi].replace("  ", " ")
                    if voittoko() != 0:
                        print(voittoko() * int(viimeisin_arvottu))
                        sys.exit()
            print(bingo_kentat)


def voittoko():  
    global jatketaan   
    #vaakatarkistus:
    for kentta in range(len(bingo_kentat)):
        for rivi in range(len(bingo_kentat[kentta])):
            if bingo_kentat[kentta][rivi].count(' *') == 5:
                print("vaakatykki")
                jatketaan = False
                return laske_summa(kentta)                

    # pystytarkistus
    for kentta in range(len(bingo_kentat)):
        pystyrivi =  []
        for ind in range(len(bingo_kentat[kentta])):
            for rivi in range(len(bingo_kentat[kentta])):
                splitted = bingo_kentat[kentta][rivi].split(" ")
                pystyrivi.append(splitted[ind])
            if pystyrivi.count('*') == 5:   
                print("pystytykki")
                jatketaan = False
                return laske_summa(kentta)                
            pystyrivi =  []
    return 0

def laske_summa(kentta):
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
