
data = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def tutki_ja_laske():
   for rivi in data:
        garbagea = False   
        i = 0
        merkkeja = 0
        g_start = 0 
        print(rivi)
        while i <= len(rivi) -1:
            if rivi[i] == "<":
                if garbagea == True:
                    merkkeja += 1
                garbagea = True
            elif rivi[i] == ">":
                if garbagea == False:
                    merkkeja += 1
                garbagea = False
            elif rivi[i] == "!":
                i += 1
            elif garbagea:
                merkkeja += 1
            i += 1
        print(merkkeja)
    


readfile()
tutki_ja_laske()
