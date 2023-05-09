
data = []

def readfile():
    global stringi
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())

def tutkiKirjainparit(kirjainparit):
    for values in kirjainparit.values():
        if len(values) > 1:
            for v1 in range(len(values) -1):
                for v2 in range(len(values)):
                    #print("v1", v1, "v2", v2)
                    erotus = values[v2] - values[v1]
                    if erotus > 1:  # 1= aaa = overlapping
                        print("erotus", erotus)
                        return True
    return False

def tutkiKirjaimet(kirjaimet):
    for values in kirjaimet.values():
        if len(values) > 1:
            for i in range(len(values) -1):
                v = values[i] 
                if v + 2 in values:
                    return True
                if v - 2 in values:
                    return True
    return False
    

def action():
    nice = 0    

    for rivi in data:
        edellinen = ""
        ind = 0
        kirjainparit = {}
        kirjaimet = {}

        for kirjain in rivi:
            if kirjain in kirjaimet:
                kirjaimet[kirjain].append(ind)
            else:
                kirjaimet[kirjain] = [ind]


            if (edellinen + kirjain) in kirjainparit:
                kirjainparit[(edellinen + kirjain)].append(ind)
            else:
                kirjainparit[(edellinen + kirjain)] = [ind]

            edellinen = kirjain
            ind += 1

        if tutkiKirjainparit(kirjainparit) and tutkiKirjaimet(kirjaimet):
            print("\n", rivi, tutkiKirjainparit(kirjainparit) and tutkiKirjaimet(kirjaimet))
            nice += 1
        else: 
            print("\n",rivi, "  Falsetti")

    return nice



readfile()
print(action())   # 59 väärin, 77 väärin, ei sanottu onko liian iso tai pieni