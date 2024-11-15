
data = []
hash = {}
hash_toisinpain = {}
oret = {}


def readfile():
    global data
    f = open("data_2.txt", "r") 
    for rivi in f:
        if 'ORE' in rivi:    # 10 ORE => 10 A
            sp = rivi.strip().split(" => ")
            oret[sp[1]] = int(sp[0].split(" ")[0])
        else:
            data.append(rivi.strip())
    data = reversed(data)


def tee_hash():
    for rivi in data:
        a, b = rivi.split(" => ")
        if "," in a:
            l = tuple(a.split(", "))
            for item in l:
                maara, kirjain = item.split(" ")
                if kirjain not in symbolit:
                    symbolit[kirjain] = 0
            hash[l] = b
            hash_toisinpain[b] = l
        else:
            hash[a] = b
            maara, kirjain = b.split(" ")
            if kirjain not in symbolit:
                symbolit[kirjain] = 0
            hash_toisinpain[b] = a
    


"""  toimii data2:

def tee_symbolit():
    for k, v in hash_toisinpain.items():
        print(k.split(" ")[1])
        if isinstance(v, tuple):
            for item in v:
                maara, kirjain = item.split(" ")
                symbolit[kirjain] += int(maara) * symbolit[k.split(" ")[1]]   """

def tee_symbolit():
    for k, v in hash_toisinpain.items():
        if isinstance(v, tuple):
            for item in v:
                kerroin_kandidaatti = 1
                maara, kirjain = item.split(" ")                
                for key in hash:
                    for item2 in key:      
                        #print(kirjain, item2)                  
                        if kirjain == item2.split(" ")[1]:
                            kerroin_kandidaatti = int(item2.split(" ")[0])
                            print(kerroin_kandidaatti, kirjain)

                symbolit[kirjain] += int(maara) * kerroin_kandidaatti


def selvita_oret():
    paljonko = 0
    for k, v in oret.items():
        maara, symboli = k.split(" ")
        kerroin = (symbolit[symboli] + int(maara) - 1) // int(maara)
        paljonko += kerroin * int(v)
        print(symboli, kerroin, paljonko)

    print(paljonko)


readfile()
print("oret", oret)
tee_hash()
print("hash", hash)
print("hash_toisinpain", hash_toisinpain)
tee_symbolit()
print(symbolit)  
selvita_oret()
#osta(100)