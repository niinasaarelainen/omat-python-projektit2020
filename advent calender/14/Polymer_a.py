data = []
muunnettava = ""
muunnokset = {}
maarat = {}

def readfile():   # a-kohta
    global data, muunnettava, muunnokset
    f = open("data.txt", "r")         
    for rivi in f:
        if "->" in rivi:
            key, value = rivi.split("->")
            muunnokset[key.strip()] = value.strip()
        elif rivi.strip() == "":
            continue
        else:
            muunnettava = rivi.strip()
    


def muunna():
    global muunnettava
    uusi_muunnettava = ""
    pit = len(muunnettava)
    for i in range(pit - 1):
        valiintuleva = muunnokset[muunnettava[i:i+2]]
        uusi_muunnettava += muunnettava[i] 
        uusi_muunnettava += valiintuleva
    uusi_muunnettava += muunnettava[pit-1]
    muunnettava = uusi_muunnettava


def laske():
    global muunnettava
    for letter in muunnettava:
        if letter not in maarat:
            maarat[letter] = muunnettava.count(letter)
    mi = min(maarat.values())
    ma = max(maarat.values())
    print(ma - mi)


readfile()
print(muunnokset, muunnettava)

for i in range(10):
    muunna()

laske()