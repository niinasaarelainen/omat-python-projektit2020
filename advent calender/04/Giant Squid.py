data = []
arvotut_numerot = []   # stringejä !!!
bingo_kentat = []
viimeisin_arvottu = None

def readfile():
    global arvotut_numerot, bingo_kentat
    f = open("data_easy2.txt", "r") 
    i = 0
    for rivi in f:
        if i == 0:
            arvotut_numerot.append(rivi.strip().split(","))
            arvotut_numerot = arvotut_numerot[0]
        else:
            if rivi.strip() == '':
               bingo_kentat.append([]) 
            else:
                bingo_kentat[-1].append(rivi.strip().replace("  ", " "))
        i += 1


def loytyyko_numero():
    global viimeisin_arvottu
    for i in range(len(arvotut_numerot)):
        viimeisin_arvottu = arvotut_numerot.pop(0).strip()
        for kentta in range(len(bingo_kentat)):
            for rivi in range(len(bingo_kentat[kentta])):
                if viimeisin_arvottu in bingo_kentat[kentta][rivi]:   #TODO  2 --> 22 --> **, pitäisi pysyä 22:na
                    bingo_kentat[kentta][rivi] = bingo_kentat[kentta][rivi].replace(viimeisin_arvottu, " * ")
                    bingo_kentat[kentta][rivi] = bingo_kentat[kentta][rivi].replace("  ", " ")
        print(bingo_kentat)


def voittoko():    
    #vaakatarkistus:
    for kentta in range(len(bingo_kentat)):
        for rivi in range(len(bingo_kentat[kentta])):
            if bingo_kentat[kentta][rivi].count(' *') == 5:
                #print("vaakatykki")
                return laske_summa(kentta)                

    # pystytarkistus
    for kentta in range(len(bingo_kentat)):
        pystyrivi =  []
        for ind in range(len(bingo_kentat[kentta])):
            for rivi in range(len(bingo_kentat[kentta])):
                splitted = bingo_kentat[kentta][rivi].split(" ")
                pystyrivi.append(splitted[ind])
            print("pystyrivi", pystyrivi)
            if pystyrivi.count('*') == 5:   
                print("pystytykki")
                return laske_summa(kentta)                
            pystyrivi =  []

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
print(voittoko() * int(viimeisin_arvottu))