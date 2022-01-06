
data = []
jarjestykset = {}
start = "G"
end = ""
vastaus = start


"""
  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----       """

def readfile():
    f = open("data_easy2.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        eka = rivi[5]
        toka = rivi[-12]
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
        return 

    print("vaihtoehtoja", vaihtoehtoja, "etsittava", etsittava)
    
    v = min(vaihtoehtoja)
    while v in vastaus:
        vaihtoehtoja.remove(v)
        if len(vaihtoehtoja) == 0:
            vastaus += etsittava
            return
        v = min(vaihtoehtoja)
    if v not in jarjestykset or v == etsittava:   # eli B ei ole avain (data.txt) ja on myös end
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
print(len(jarjestykset)) #!!! vastauksetn pitäisi olla 25 kirjainta !!!
for k, values in jarjestykset.items():
    for v in values:
        if v != " " and v not in jarjestykset:
            end = v
print("end", end)
print(etsi(start, jarjestykset[start]))
print(vastaus+end)    #!!! vastauksetn pitäisi olla 25 kirjainta !!!