
data = []

def readfile():
    global stringi
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())

def tutkiKirjainparit(kirjainparit):
    print(kirjainparit)
    for values in kirjainparit.values():
        if len(values) > 1:
            values = sorted(values)
            print(values)
            for i in range(len(values) -1):
                erotus = values[i +1] - values[i]
                if erotus >= 1:  # 1= aaa = overlapping
                    return True

def tutkiKirjaimet(kirjaimet):
    print(kirjaimet)
    for values in kirjaimet.values():
        if len(values) > 1:
            for i in range(len(values) -1):
                v = values[i] 
                if v + 2 in values:
                    return True
                if v - 2 in values:
                    return True
    

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
            nice += 1

    return nice



readfile()
print(data)
print(action())   # 59 väärin, 77 väärin