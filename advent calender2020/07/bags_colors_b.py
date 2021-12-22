

laukkujen_sisalto = {}
polut = []
laukkuja_yht = 0


def readfile():   
    f = open("data_easy.txt", "r")         
    for rivi in f:
        split1 = rivi.split(" bags contain ")
        laukkujen_sisalto[split1[0]] = split1[1].strip().split(", ")

    #print(laukkujen_sisalto)

"""
def kay_lapi(solmu, polku): 
    global laukkuja_yht

    if "other bags" in solmu:
        print('->'.join(polku))
        polut.append(polku)
        return 
    
    polku.append(solmu)
    
    for s in laukkujen_sisalto[solmu]:  # = seuraajat
        uusi_polku = polku[:]
        splitted = s.split(" ")
        s = splitted[1] + " " + splitted[2]
        if splitted[0] != "no":
            laukkuja_yht += int(splitted[0])
        print(laukkuja_yht)
        kay_lapi(s, uusi_polku)  """


def kay_lapi(solmu, polku, lkm): 
    global laukkuja_yht

    print("lkm alussa: ",  lkm)

    if "other bags" in solmu:
        print('->'.join(polku))
        laukkuja_yht += lkm
        polut.append(polku)
        return 
    
    polku.append(solmu)
    
    for s in laukkujen_sisalto[solmu]:  # = seuraajat
        uusi_polku = polku[:]
        splitted = s.split(" ")
        s = splitted[1] + " " + splitted[2]
        if splitted[0] != "no":
            lkm *= int(splitted[0])
            print(lkm, int(splitted[0]))
        kay_lapi(s, uusi_polku, lkm)  
        """
        if splitted[0] != "no":
            lkm = int(splitted[0]) """

 
def muodosta_dict():
    laukkujen_sisalto_key_on_value = {}
    for l, laukut in laukkujen_sisalto.items():
        total = 0
        for laukku in laukut:        
            splitted = laukku.split(" ")
            laukku = splitted[1] + " " + splitted[2]
            if splitted[0] != "no":
                lkm = int(splitted[0])
                total += lkm
        laukkujen_sisalto_key_on_value[l] = total
    print(laukkujen_sisalto_key_on_value)


def etsi():
    pass


readfile()
#kay_lapi("shiny gold", [], 1)
etsi()
print(laukkuja_yht)
