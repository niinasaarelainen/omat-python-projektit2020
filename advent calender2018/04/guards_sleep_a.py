
guards = {}  # id : {minutes: sleep}
guards_parempi = {}


def readfile():
    f = open("data.txt", "r")    # [1518-11-01 00:00] Guard #10 begins shift
    kenesta_vartijasta_kyse = None
    for rivi in f:

        if "#" in rivi:
            sp = rivi.strip().split("#")
            kellonaika = rivi.strip().split(":")
            kellonaika = kellonaika[1][:2]
            kenesta_vartijasta_kyse = sp[1].split(" ")[0]
            if kenesta_vartijasta_kyse in guards:
                guards[kenesta_vartijasta_kyse] += [kellonaika, sp[1]]
            else: 
                guards[kenesta_vartijasta_kyse] = [kellonaika, sp[1]]
        else:   
            sp = rivi.strip().split(":")
            kellonaika = sp[1][:2]
            if kenesta_vartijasta_kyse in guards:
                guards[kenesta_vartijasta_kyse] += [kellonaika, sp[1]]
            else:
                guards[kenesta_vartijasta_kyse] = [kellonaika, sp[1]]  
    

def luo_guards_parempi():
    global guards_parempi
    for g in guards:
        guards_parempi[g] = [] 


def kasittele():
    global guards_parempi  # id : [nukkumisminuutti, nukkumisminuutti]
    for id, tiedot in guards.items():
        for i in range(0, len(tiedot) -1, 2):
            if "begins" in tiedot[i + 1]:
                pass
            elif "falls" in tiedot[i + 1]:
                guards_parempi[id].append(int(tiedot[i]))
            elif "wakes" in tiedot[i + 1]:
                #print("vika entree:",guards_parempi[id][-1] )
                for minute in range(guards_parempi[id][-1] + 1, int(tiedot[i]) ):
                    guards_parempi[id].append(minute)


def laske_maarat(minuutit):
    print(minuutit)
    tulos = max([(minuutit.count(minut), minut)  for minut in minuutit])
    print("tulos: ", tulos)   

    return tulos[1]




readfile()
luo_guards_parempi()

kasittele()
print(guards_parempi)


eniten_nukkumista = max([(len(tiedot), id)  for id, tiedot in guards_parempi.items()])
id = eniten_nukkumista[1]

minuutti = laske_maarat(guards_parempi[id])
print(minuutti * int(id))
