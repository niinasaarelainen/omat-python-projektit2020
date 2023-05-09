decompressed = 0
data = []


def readfile():
    f = open("data_1.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def tutki(rivi):
            global decompressed
            print(rivi, decompressed)
            i = 0
            eka_sulku_alk = rivi.index("(")   
            eka_sulku_lop = rivi.index(")")  
            uusi_alkoituskohta = eka_sulku_lop + 1
            decompressed += eka_sulku_lop   

            ohje = rivi[eka_sulku_alk + 1:eka_sulku_lop]
            print(ohje)
            montako_kirjainta, montako_kertaa = ohje.split("x")
            kerataan_sanaa = rivi[eka_sulku_lop+1:eka_sulku_lop+1+ int(montako_kirjainta)]
            print(" kerataan_sanaa: ", kerataan_sanaa )
            ohje_suluilla = rivi[eka_sulku_alk :eka_sulku_lop + 1]
            if "(" in kerataan_sanaa:
                rivi = rivi.replace(ohje_suluilla, kerataan_sanaa * (int(montako_kertaa) - 1))
            else:
                decompressed += int(montako_kirjainta) * int(montako_kertaa)
                uusi_alkoituskohta += int(montako_kirjainta) 
            
            if "(" in rivi[uusi_alkoituskohta :]:                              
                tutki(rivi[uusi_alkoituskohta :])
            else:
                 print(rivi, len(rivi))
                 print(decompressed)

readfile()
tutki(data[0])
