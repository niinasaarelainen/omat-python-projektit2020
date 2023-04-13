
data = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def tutki():

    for rivi in data:
        i = 0
        decompressed = ""
        ohje_alkanut = False
        while True:
            if rivi[i] == ")":     # A(1x5)BC
                ohje_alkanut = False
                montako_kirjainta, montako_kertaa = ohje.split("x")
                kerataan_sanaa = ""
                for montako in range(int(montako_kirjainta)):
                    i += 1
                    kerataan_sanaa += (rivi[i])
                    
                decompressed += int(montako_kertaa) * kerataan_sanaa
            elif ohje_alkanut:
                ohje += rivi[i]
            elif rivi[i] == "(":     # A(1x5)BC
                ohje = ""
                ohje_alkanut = True
            else:
                decompressed += rivi[i]
            
            if i <  len(rivi) - 1:
                i += 1
            else:
                break

        print(decompressed, len(decompressed))


readfile()
tutki()
