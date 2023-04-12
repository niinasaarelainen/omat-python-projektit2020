data = []
sana_muistiin = []


def readfile():
    global data
    f = open("data.txt", "r")    
    
    for rivi in f:
        data.append(rivi.strip().split("["))


def cipher(sana, maara):
    maara_orig = maara
    maara = maara % 26
    sana_muistiin = []
    for letter in sana:  
        luku = ord(letter) + maara
        if luku > 122:
            luku = 97 +  (luku - 123)       
        sana_muistiin.append((chr(luku)))  # ord('a') = 97     cipher     TUTKI
    if ("north" in "".join(sana_muistiin)):
        print ("JEE", maara_orig, "".join(sana_muistiin))
    
def count():
    ID_sum = 0

    for rivi in data:
        kirjaimet = {}
        ok = True

        items = rivi[0].split("-")
        checksum = rivi[1]
        id = int(items[-1])
        #print(id, checksum)
        items.remove(items[-1])
        for item in items:
            cipher(item, id)
            for merkki in item:
                if merkki not in kirjaimet:
                    kirjaimet[merkki] = 1
                else:
                    kirjaimet[merkki] += 1     
        
        
        kirjaimet = dict(sorted(kirjaimet.items(), key=lambda item: (-item[1], item[0])))
        montako = 1
        for aakkonen in kirjaimet.keys():
            if aakkonen not in checksum:
                ok = False
                break
            montako += 1
            if montako > 5:
                break
        if ok: 
            ID_sum += id
    
    return ID_sum
        




readfile()
print(count())