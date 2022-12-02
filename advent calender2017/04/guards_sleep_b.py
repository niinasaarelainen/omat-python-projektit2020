data = []
guards = {}  # id : {minutes: sleep}
guards_parempi = {}



def readfile():
    global data
    f = open("data.txt", "r")    # [1518-11-01 00:00] Guard #10 begins shift
    
    for rivi in f:
        data.append(rivi.strip())
    data = sorted(data)

    kenesta_vartijasta_kyse = None
    for rivi in data:
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


def laske_maarat():
    tulokset = []
    for id, mins in guards_parempi.items():
        if mins != []:
            tulos = max([(mins.count(minut), minut, id) for minut in mins ])
            print("tulos: ", tulos)  
            tulokset.append(tulos) 

    return max(tulokset)




readfile()
luo_guards_parempi()
print(guards)

kasittele()
print(guards_parempi)

maara, minuutti, id = laske_maarat()
print(minuutti * int(id))  
