import math

data = []
dirs_alahakemistot = {}
dirs_luvut = {}
dirs_summat = {}
mika_hakemisto = []


def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())
        if "dir" in rivi:
            dirs_alahakemistot[rivi.split(" ")[1].strip()] = []
            dirs_luvut[rivi.split(" ")[1].strip()] = []

"""a has total size 94853  : contains files f (size 29116), g (size 2557), and h.lst (size 62596) 
plus file i indirectly (a contains e which contains i) """


def tutkiTemp(temp, mika_dir):
    for rivi in temp:
        luku = 0
        if "dir" in rivi:
            alahakemisto = rivi.split(" ")[1]
            dirs_alahakemistot[mika_dir].append(alahakemisto)
        else:
            sp = rivi.split(" ")
            for s in sp:
                if s.isdigit():
                    luku += int(s)
        dirs_luvut[mika_dir].append(luku)

def tutki_cd():
    talteen = False
    temp = []
    for rivi in data:
        if ".."  in rivi :
            dir = mika_hakemisto.pop(-1)
            print("..", temp, dir)
            tutkiTemp(temp, dir)  
            temp = []
            talteen = False
        if ("cd" in rivi and talteen ):
            mika_hakemisto.append(dir)   
            print("cd True", temp, mika_hakemisto[-1])
            tutkiTemp(temp, mika_hakemisto[-1])
            temp = []
            talteen = False
        if "cd" in rivi and talteen == False:  
            #print("if cd in rivi and talteen == False: ")          
            sp = rivi.split(" ")
            dir = sp[-1]
            if dir in dirs_luvut.keys():
                talteen = True    
                mika_hakemisto.append(dir)   
        if talteen:        
            temp.append(rivi)
    tutkiTemp(temp, mika_hakemisto[-1])
    print(temp)


def summat():
    for k in dirs_luvut:
        summa = sum(dirs_luvut[k])
        for v in dirs_alahakemistot[k]:           
            summa += sum(dirs_luvut[v])
        dirs_summat[k] = int(summa)


readfile()
tutki_cd()
#print(dirs_luvut)
print(dirs_alahakemistot)
summat()
#print(dirs_summat)
vastaus = [s for s in dirs_summat.values() if s <= 100000]
print("hak.maara", len(vastaus))
print(sum(vastaus))       # too low 982555
