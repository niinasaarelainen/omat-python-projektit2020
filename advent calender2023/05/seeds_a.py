import copy

data = []
seeds_nykyiset = [79, 14, 55, 13]
#seeds_nykyiset = [81, 53, 57, 52]
#seeds_nykyiset = [280775197,7535297,3229061264,27275209,77896732,178275214,2748861189,424413807,3663093536,130341162,613340959,352550713,1532286286,1115055792,1075412586,241030710,3430371306,138606714,412141395,146351614]
dest_rang_st = []      
source_rang_st = []    # näihin 1 map kerrallaan
range_length = []

dest_rang_st_ALL = []      
source_rang_st_ALL = []    # näihin 7 mappia, kukin oma list
range_length_ALL = []



def readfile():
    #  50                98                2
    # dest rang st      source rang st     range length
    f = open("data_1_small.txt", "r") 
    for rivi in f:
        data.append(rivi)   

def kayLapi():
    global  dest_rang_st, source_rang_st, range_length    

    for rivi in data:
        if rivi == "\n":
            dest_rang_st_ALL.append(dest_rang_st)
            source_rang_st_ALL.append(source_rang_st)   # näihin 7 mappia, kukin oma list
            range_length_ALL.append(range_length)
            dest_rang_st = []      
            source_rang_st = []    # näihin 1 map kerrallaan
            range_length = []
        else:
            rivi = rivi.strip().split(" ")
            dest_rang_st.append(int(rivi[0]))      
            source_rang_st.append(int(rivi[1]))    
            range_length.append(int(rivi[2]))   

    #lopuksi:
    dest_rang_st_ALL.append(dest_rang_st)
    source_rang_st_ALL.append(source_rang_st)   # näihin 7 mappia, kukin oma list
    range_length_ALL.append(range_length)


     


def corresponds():   
    global seeds_nykyiset
    for vaihe_nro in range(len(dest_rang_st_ALL)):
        dest_rang_st = dest_rang_st_ALL[vaihe_nro]      
        source_rang_st = source_rang_st_ALL[vaihe_nro]    # näihin 1 map kerrallaan
        range_length = range_length_ALL[vaihe_nro]

        kuinka_kauan = 0
        print(seeds_nykyiset)
        seeds_uudet = []
        for seed in seeds_nykyiset:
            print()
            # lähin edeltäjä:
            etaisyydet = []
            for s in source_rang_st:
                if seed -s >= 0:
                    etaisyydet.append(s)
            print("max(etaisyydet))", max(etaisyydet))
            tulos =  max(etaisyydet)

            index = source_rang_st.index(tulos)
            print("index", index)

            #laske  onko yllä oleva voimassa, sitten erotus
            # tai jos ei voimassa, seeds_uudet.append(seed)  

           
            alku = source_rang_st[index]
            vastaa = dest_rang_st[index]
            kuinka_kauan = range_length[index]
            seedin_lopetusLuku = alku + kuinka_kauan + 1
            print("seed", seed, ", seedin_lopetusLuku", seedin_lopetusLuku)
            
            if seed >= alku and seed < seedin_lopetusLuku:
                seeds_uudet.append(seed + (vastaa - alku))
            else:
                seeds_uudet.append(seed)  

        seeds_nykyiset = copy.deepcopy(seeds_uudet) 
        print("seeds_nykyiset", seeds_nykyiset)



readfile()
kayLapi()
print(dest_rang_st, source_rang_st, range_length)
corresponds()
print("vastaus:", min(seeds_nykyiset))