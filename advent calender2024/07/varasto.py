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
