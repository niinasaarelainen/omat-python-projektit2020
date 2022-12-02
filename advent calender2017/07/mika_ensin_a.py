
data = []
jarjestykset = {}
start = "L"
end = ""
vastaus = ""
avaimet = []
valuet = []



"""
  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----       """

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        eka = rivi[5]
        toka = rivi[-12]
        avaimet.append(eka)
        valuet.append(toka)
        if eka in jarjestykset:
            jarjestykset[eka].append(toka)
        else:
            jarjestykset[eka] = [toka]



def etsi(etsittava, vaihtoehtoja):
    global end, vastaus    
    
    vaihtoehtoja = vaihtoehtoja + jarjestykset[etsittava]
    vaihtoehtoja = list(dict.fromkeys(vaihtoehtoja)) 
    if etsittava in vaihtoehtoja :
        vaihtoehtoja.remove(etsittava)
        if len(vaihtoehtoja) == 0:
            return
    if end in vaihtoehtoja and len(vaihtoehtoja) == 1:
        vastaus += etsittava
        return 

    print("vaihtoehtoja", vaihtoehtoja, "etsittava", etsittava)
    
    v = min(vaihtoehtoja)
    while v in vastaus:
        vaihtoehtoja.remove(v)
        if len(vaihtoehtoja) == 0:
            #vastaus += etsittava
            return
        v = min(vaihtoehtoja)
    if v not in jarjestykset or v == etsittava:   # eli B ei ole avain (data.txt) ja on myös end
        print("if v not in jarjestykset", v)
        vaihtoehtoja.remove(v)
        v = min(vaihtoehtoja)
        if v not in vastaus:
            vastaus += v
        print("ifissä uusi v", v)
        #if v == end:
        #    return
        etsi(v, vaihtoehtoja)
       
    else:        
        vaihtoehtoja.remove(v)
        vastaus += v
        print(etsittava, v)
        etsi(v, vaihtoehtoja)

def etsi_alut():
    alut = []
    for k, values in jarjestykset.items():
        if k not in valuet:
            alut.append(k)
    return alut

def etsi_loput():
    loput = []
    for k, values in jarjestykset.items():
        for v in values:
            if v not in jarjestykset:
                loput.append(v)
    return loput


readfile()
for item in sorted(jarjestykset.items()):
    print(item)         
#print(len(jarjestykset)) #!!! vastauksetn pitäisi olla 25 kirjainta !!!
avaimet = list(dict.fromkeys(avaimet)) 
valuet = list(dict.fromkeys(valuet)) 
loput = etsi_loput()  # B
end = loput[0]
alut = etsi_alut()   # ['G', 'L', 'J', 'N']

"""
start = "N"
vastaus = start
print("\n start = N")
print(etsi(start, ['G', 'L', 'J']))
print(vastaus+end)    #!!! vastauksetn pitäisi olla 25/ 26 kirjainta !!!
print(len(vastaus+end))

start = "L"
vastaus = start
print("\n start = L")
print(etsi(start, ['G', 'J', 'N']))
print(vastaus+end)    #!!! vastauksetn pitäisi olla 25 / 26 kirjainta !!!
print(len(vastaus+end))   """

start = "G"
vastaus = start
print("\n start = G")
print(etsi(start, ['J', 'L', 'N', 'T']))
print(vastaus+end)    #!!! vastauksetn pitäisi olla 25 / 26 kirjainta !!!
print(len(vastaus+end))    

tulos =  "GJICKLDFEHNAOPQRSTMUVWXYZB"
tulos2 = "GJICKLDFEHNAOPQRSTMUVWXYZB"
print(tulos == tulos2)
print( [ c for c in tulos if tulos.count(c) > 1])