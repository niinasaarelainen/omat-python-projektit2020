
data = []
seeds = {79:[], 14:[], 55:[], 13:[]}
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

def corresponds(): 
    for vaihe_nro in range(len(dest_rang_st_ALL)):
        dest_rang_st = dest_rang_st_ALL[vaihe_nro]      
        source_rang_st = source_rang_st_ALL[vaihe_nro]    # näihin 1 map kerrallaan
        range_length = range_length_ALL[vaihe_nro]

        kuinka_kauan = 0
        kuinka_kauan_mennyt = 0
        for nro in range(max(seeds)+1):
            
            if nro in source_rang_st:
                index = source_rang_st.index(nro)
                vastaa = dest_rang_st[index]
                kuinka_kauan = range_length[index]
            kuinka_kauan_mennyt = 0
        if kuinka_kauan - kuinka_kauan_mennyt > 0:
            print(nro, vastaa + kuinka_kauan_mennyt)
            kuinka_kauan_mennyt += 1
            if nro  in seeds:
                seeds[nro].append(vastaa + kuinka_kauan_mennyt)
        elif nro in seeds:
                seeds[nro].append(nro)          



readfile()
kayLapi()
print(dest_rang_st, source_rang_st, range_length)
corresponds()
print(seeds)