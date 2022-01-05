
data = []
jarjestykset = {}
start = "C"
end = ""
vastaus = start


"""
  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----       """

def readfile():
    f = open("data_easy.txt", "r") 
    for rivi in f:
        eka = rivi[5]
        toka = rivi[-13]
        if eka in jarjestykset:
            jarjestykset[eka].append(toka)
        else:
            jarjestykset[eka] = [toka]


def etsi(etsittava, vaihtoehtoja):
    global end, vastaus    
    
    vaihtoehtoja = vaihtoehtoja + jarjestykset[etsittava]
    vaihtoehtoja = list(dict.fromkeys(vaihtoehtoja))
    if vaihtoehtoja[0] == end and len(vaihtoehtoja) == 1:
        return
    print("vaihtoehtoja", vaihtoehtoja, "etsittava", etsittava)
    v = min(vaihtoehtoja)
    if v not in jarjestykset:
        vastaus += v
        vaihtoehtoja.remove(v)
        v = min(vaihtoehtoja)
        if v == end:
            return
        etsi(v, vaihtoehtoja)
       
    else:        
        vaihtoehtoja.remove(v)
        vastaus += v
        print(etsittava, v)
        etsi(v, vaihtoehtoja)



readfile()
print(jarjestykset)
for k, values in jarjestykset.items():
    for v in values:
        if v != " " and v not in jarjestykset:
            end = v
print("end", end)
print(etsi(start, jarjestykset[start]))
print(vastaus+end)