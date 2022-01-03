
data = []
keys = []
doors = []
kohteet = []
olet_nyt_tassa = []

def readfile():
    f = open("data_easy.txt", "r") 
    for rivi in f:
        data.append([])
        for merkki in rivi.strip():
            data[-1].append(merkki)

 
def find_keys_and_doors():
    for rivi in range(len(data)):
        for merkki in range(len(data[rivi])):
           if data[rivi][merkki] in ['#', '.']:
               pass
           elif data[rivi][merkki] == '@':
               olet_nyt_tassa.append(rivi)
               olet_nyt_tassa.append(merkki) 
           elif data[rivi][merkki].lower() == data[rivi][merkki]:
               keys.append([rivi, merkki])
           else:
               doors.append([rivi, merkki])
    

def calculate_distances(y, x):
    pienin_k = 1000
    pienin_key = keys[0]
    for key in keys:
        if key[0] == y:
            if abs(key[1] - x) < pienin_k:
                pienin_k = abs(key[1] - x)
                pienin_key = key
    print(pienin_k, pienin_key)


readfile()
print(data)
find_keys_and_doors()
print("alkupiste", olet_nyt_tassa)
print("keys: ", keys)
print("doors: ", doors)
calculate_distances(olet_nyt_tassa[0], olet_nyt_tassa[1])
