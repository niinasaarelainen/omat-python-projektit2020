def etsi(l, lkm):
    global laukkuja_yht
    for laukku in laukkujen_sisalto[l]:
        print(laukku)        
        if "other bags" in laukku:
            lkm = 0
            break
        splitted = laukku.split(" ")
        laukku = splitted[1] + " " + splitted[2]
        if splitted[0] != "no":
            lkm += int(splitted[0])
        laukkuja_yht += lkm * laukkujen_sisalto_key_on_value[laukku]
        print(lkm * laukkujen_sisalto_key_on_value[laukku])
        etsi(laukku, lkm)
        