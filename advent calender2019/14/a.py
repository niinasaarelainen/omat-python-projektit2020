
data = []
hash = {}
hash_toisinpain = {}
symbolit = {'FUEL' : 1}
oret = {}


def readfile():
    global data
    f = open("data_2.txt", "r") 
    for rivi in f:
        if 'ORE' in rivi:    # 10 ORE => 10 A
            sp = rivi.strip().split(" => ")
            oret[sp[1]] = int(sp[0].split(" ")[0])
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
    


"""10 ORE => 10 A
1 ORE => 1 B"""

def tee_symbolit():
    for k, v in hash_toisinpain.items():
        print(k.split(" ")[1])
        if isinstance(v, tuple):
            for item in v:
                maara, kirjain = item.split(" ")
                symbolit[kirjain] += int(maara) * symbolit[k.split(" ")[1]]

        # {'A': 4, 'B': 9, 'C': 11, 'AB': 2, 'BC': 3, 'CA': 4}


def selvita_fuel():
    pass


readfile()
print("oret", oret)
tee_hash()
print("hash", hash)
print("hash_toisinpain", hash_toisinpain)
tee_symbolit()
print(symbolit)    
selvita_fuel() 
#osta(100)