data = []


def readfile():
    global data
    f = open("data.txt", "r")    
    
    for rivi in f:
        data.append(rivi.strip().split("["))


    
def count():
    ID_sum = 0

    for rivi in data:
        kirjaimet = {}
        ok = True

        items = rivi[0].split("-")
        checksum = rivi[1]
        id = int(items[-1])
        print(id, checksum)
        items.remove(items[-1])
        for item in items:
            for merkki in item:
                if merkki not in kirjaimet:
                    kirjaimet[merkki] = 1
                else:
                    kirjaimet[merkki] += 1     
        
        print(kirjaimet, "ei järj")
        kirjaimet = dict(sorted(kirjaimet.items(), key=lambda item: (-item[1], item[0])))
        print(kirjaimet, "järj")
        montako = 1
        for aakkonen in kirjaimet.keys():
            print("aak", aakkonen)
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
print(data)
print(count())