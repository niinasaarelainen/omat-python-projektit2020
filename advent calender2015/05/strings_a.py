
data = []


def readfile():
    global stringi
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def action():

    kielletyt = ["ab", "cd", "pq", "xy"]
    nice = 0
    

    for rivi in data:
        edellinen = ""
        vokaalia = 0
        tupla = False
        kielletty_loytyi = False

        for kirjain in rivi:
            if kirjain in "aeiou":
                vokaalia += 1
            if kirjain == edellinen:                
                tupla = True
            for k in kielletyt:
                if edellinen+kirjain == k:
                    kielletty_loytyi = True
            edellinen = kirjain

        if vokaalia >= 3 and tupla and kielletty_loytyi == False:
            nice += 1

    return nice


readfile()
print(data)
print(action())
 
 