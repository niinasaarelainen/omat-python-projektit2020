


def readfile():   
    f = open("data_easy.txt", "r")         
    for rivi in f:
        split1 = rivi.split(" bags contain ")
        laukkujen_sisalto[split1[0]] = split1[1].strip().split(", ")


"""
def kay_lapi(solmu, polku, lkm): 
    global laukkuja_yht, laukkujen_sisalto_key_on_value

    print("lkm alussa: ",  lkm)

    if "other bags" in solmu:
        print('->'.join(polku))
        laukkuja_yht += lkm + 1
        polut.append(polku)
        return 
    
    polku.append(solmu)
    
    for s in laukkujen_sisalto[solmu]:  # = seuraajat
        uusi_polku = polku[:]
        splitted = s.split(" ")
        s = splitted[1] + " " + splitted[2]
        if splitted[0] != "no":
            lkm += laukkujen_sisalto_key_on_value[s] * int(splitted[0]) 
            print(lkm, int(splitted[0]))
        kay_lapi(s, uusi_polku, lkm)  
        if splitted[0] != "no":
            lkm = int(splitted[0])   """

 
def muodosta_dict():
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

"""
def etsi(l):   # easy toimii, b ei: tulee 22, pitäisi tulla 126
    global laukkuja_yht
    
    for laukku in laukkujen_sisalto[l]:
        print(laukku)
        
        if "other bags" in laukku:
            break
        splitted = laukku.split(" ")
        laukku = splitted[1] + " " + splitted[2]
        if splitted[0] != "no":
            lkm = int(splitted[0])
        laukkuja_yht += lkm * laukkujen_sisalto_key_on_value[laukku]
        print(lkm * laukkujen_sisalto_key_on_value[laukku])
        etsi(laukku)    """
        
def etsi(l, lkm, max):    # TODO
    global laukkuja_max
    for laukku in laukkujen_sisalto[l]:
              
        if "other bags" in laukku:
            break
        splitted = laukku.split(" ")
        laukku = splitted[1] + " " + splitted[2]
        if splitted[0] != "no":
            lkm += int(splitted[0])
            lkm *=  laukkujen_sisalto_key_on_value[laukku]   
            if lkm > laukkuja_max:
                laukkuja_max = lkm
        etsi(laukku, lkm, laukkuja_max)
    print("lopussa max", laukkuja_max )
        


laukkujen_sisalto_key_on_value = {}
laukkujen_sisalto = {}
polut = []
laukkuja_max = 0

readfile()
muodosta_dict()
#print(len(laukkujen_sisalto_key_on_value))
#kay_lapi("shiny gold", [], 1)
etsi("shiny gold", 0, 0)
laukkuja_max += laukkujen_sisalto_key_on_value["shiny gold"]
print("laukkuja_yht", laukkuja_max)   # 837  too low
