import math

data = []
dirs_alahakemistot = {}
dirs_luvut = {}
dirs_summat = {}


def readfile():   
    f = open("data_a2.txt", "r")         
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
    mika_dir = ""
    temp = []
    for rivi in data:
        if (".."  in rivi and talteen) or ("cd" in rivi and talteen ):
            print(temp)
            tutkiTemp(temp, mika_dir)  # pitäisi olla 'a': ['e']  !!!!!!!!!!!!!!!!!!!!
            temp = []
            talteen = False
        if "cd" in rivi and talteen == False:            
            sp = rivi.split(" ")
            dir = sp[-1]
            if dir in dirs_luvut.keys():
                talteen = True    
                mika_dir = dir   
        if talteen:        
            temp.append(rivi)
    tutkiTemp(temp, mika_dir)
    print(temp)


def summat():
    for k in dirs_luvut:
        summa = sum(dirs_luvut[k])
        for v in dirs_alahakemistot[k]:           
            summa += sum(dirs_luvut[v])
        dirs_summat[k] = int(summa)


readfile()
tutki_cd()
print(dirs_luvut)
print(dirs_alahakemistot)
summat()
print()
vastaus = [s for s in dirs_summat.values() if s <= 100000]
print(sum(vastaus))
