import copy

data = []
seeds_nykyiset = [79, 14, 55, 13]
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
    f = open("data_1.txt", "r") 
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
        kuinka_kauan_mennyt = 0
        print(seeds_nykyiset)
        seeds_uudet = []
        for nro in range(max(seeds_nykyiset)+1):
            print(nro)
            if nro in source_rang_st:
                index = source_rang_st.index(nro)
                vastaa = dest_rang_st[index]
                kuinka_kauan = range_length[index]
                kuinka_kauan_mennyt = 0

            if kuinka_kauan - kuinka_kauan_mennyt > 0:
                #print(nro, vastaa + kuinka_kauan_mennyt)                
                if nro  in seeds_nykyiset:
                    seeds_uudet.append(vastaa + kuinka_kauan_mennyt)
                kuinka_kauan_mennyt += 1            
            elif nro in seeds_nykyiset:
                    seeds_uudet.append(nro)  

        seeds_nykyiset = copy.deepcopy(seeds_uudet)



readfile()
kayLapi()
print(dest_rang_st, source_rang_st, range_length)
corresponds()
print(seeds_nykyiset)
print("vastaus:", min(seeds_nykyiset))