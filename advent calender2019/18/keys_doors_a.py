
data = []
olet_nyt_tassa_x = 0
olet_nyt_tassa_y = 0
askeleet = 0
askeleet_kaikki = []

def readfile():
    global olet_nyt_tassa_x, olet_nyt_tassa_y
    f = open("data_easy.txt", "r") 
    i = 0
    for rivi in f:
        data.append([])
        j = 0
        for merkki in rivi.strip():
            data[-1].append(merkki)
            if merkki == "@":
                olet_nyt_tassa_y = i
                olet_nyt_tassa_x = j
            j += 1
        i += 1

 
def find_2_lahinta(y, x):
    global askeleet
    lahimmat_avaimet = {}  # avaimen x : askeleet @:sta

    # oikealle:
    if x < len(data[y]) -1:
        for merkki in range(x +1, len(data[y])):            
            if data[y][merkki] in ['.', '#']:
                pass 
            elif data[y][merkki].islower():
                lahimmat_avaimet[(data[y][merkki])] = abs(merkki - x)
                break
            else: 
                break
        

    # vasemmalle
    if x > 0:
        for merkki in range(x - 1, -1, -1):
            if data[y][merkki] in ['.', '#']:
                pass 
            elif data[y][merkki].islower():
                lahimmat_avaimet[(data[y][merkki])] = abs(merkki - x)
                break
            else:
                break

    return lahimmat_avaimet
    




readfile()
print(data)
print("olet_nyt_tassa_y, olet_nyt_tassa_x", olet_nyt_tassa_y, olet_nyt_tassa_x)
avaimet = find_2_lahinta(olet_nyt_tassa_y, olet_nyt_tassa_x)
#avaimet = find_2_lahinta(1, 3)
for avain in avaimet:
    ind = data[olet_nyt_tassa_y].index(avain)
    olet_nyt_tassa_x = ind
    data[olet_nyt_tassa_y][ind] = "."
    askeleet += avaimet[avain]
    
    ind = data[olet_nyt_tassa_y].index(avain.upper())
    data[olet_nyt_tassa_y][ind] = "."
print(data)
print("askeleet", askeleet)
