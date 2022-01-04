
data = []
olet_nyt_tassa_x = 0
olet_nyt_tassa_y = 0
askeleet_kaikki = []

def readfile():
    global olet_nyt_tassa_x, olet_nyt_tassa_y
    f = open("data_easy2.txt", "r") 
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

 



def avain_eri_kerroksessa(y_orig, x_orig):
    y = y_orig
    x = x_orig
    lahimmat_avaimet = {}  # avaimen x : askeleet @:sta
    suunta = None
    # oikealle & alas ja ylös:
    askeleet = 0
    if x < len(data[y]) -1 and y < len(data) - 1:
        for merkki in range(x +1, len(data[y])):            
            if data[y][merkki]  == '.' :
                askeleet += 1   
            elif data[y][merkki].islower():
                    print("askeleet#", askeleet, y, merkki)   
                    askeleet += 1
                    lahimmat_avaimet[(data[y][merkki])] = askeleet  
                    break       
            # törmättiin oikeaan seinään      
            elif data[y][merkki] == '#': 
                if data[y + 1][merkki - 1]  == '.':
                    suunta = "alas" 
                if data[y - 1][merkki - 1]  == '.':
                    suunta = "ylös"  

                if suunta == "alas":   
                    merkki -= 1  
                    y += 1                   
                    while data[y][merkki]  == '.':                   
                        y += 1
                        askeleet += 1                    
                    merkki -= 1
                    y -= 1
                    while data[y][merkki]  == '.':                    
                        merkki -= 1
                        askeleet += 1

                if suunta == "ylös":   
                    merkki -= 1  
                    y -= 1                   
                    while data[y][merkki]  == '.':                   
                        y -= 1
                        askeleet += 1                    
                    merkki -= 1
                    y += 1
                    while data[y][merkki]  == '.':                    
                        merkki -= 1
                        askeleet += 1
                    
                if data[y][merkki].islower():
                    print("askeleet#", askeleet, y, merkki)   
                    askeleet += 1
                    lahimmat_avaimet[(data[y][merkki])] = askeleet  
                    break
            else: 
                break

    # vasemmalle & alas  TODO oikealle & ylös, vas & alas    
    askeleet = 0
    y = y_orig
    x = x_orig
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
    

def etsi_kirjainpari(k):
    global data, olet_nyt_tassa_x, olet_nyt_tassa_y
    key = []
    #print(" k @ etsi_iso_kirjainpari", k)

    r = 0
    for rivi in data:
        c = 0
        for char in rivi:            
            if data[r][c] == k.upper():
                data[r][c] = "."
            if data[r][c] == k:
                data[r][c] = "@"
                olet_nyt_tassa_x = c
                olet_nyt_tassa_y = r
            c += 1  
        r += 1  

def loytyi_2_avainta(avaimet_eri_kerros, askeleet):
    eka = ""
    askeleet_local = askeleet

    # eka kombo
    for key in avaimet_eri_kerros:
        print("eka kombo key", key)
        eka = key
        etsi_kirjainpari(key)
        askeleet_local += avaimet_eri_kerros[key]
        
        print(data[1])
        print(data[3])
        data[olet_nyt_tassa_y][olet_nyt_tassa_x] = "."
    askeleet_kaikki.append(askeleet)

    # toka kombo    # TODO tässä pitäisi palauttaa tilanne  ENNEN ekaa komboa !!!!!!!!!!!!!!!!!!!!!
    askeleet_local = askeleet
    print("toka kombo key", eka)
    etsi_kirjainpari(eka)    
    askeleet_local += avaimet_eri_kerros[eka]
    k = avaimet_eri_kerros.pop(eka)
    print("avaimet_eri_kerros pop", avaimet_eri_kerros)
    
    print(data[1])
    print(data[3])
    data[olet_nyt_tassa_y][olet_nyt_tassa_x] = "."
    for key in avaimet_eri_kerros:   # jäljellä enää 1
        etsi_kirjainpari(key)
        askeleet_local += avaimet_eri_kerros[key]
        
        print(data[1])
        print(data[3])
        data[olet_nyt_tassa_y][olet_nyt_tassa_x] = "."
    askeleet_kaikki.append(askeleet)
    print("      askeleet_kaikki", askeleet_kaikki)

def main():
    global olet_nyt_tassa_y, olet_nyt_tassa_x
    askeleet = 0
    for i in range(8):
        print("olet_nyt_tassa_y, olet_nyt_tassa_x", olet_nyt_tassa_y, olet_nyt_tassa_x)
        avaimet_eri_kerros = avain_eri_kerroksessa(olet_nyt_tassa_y, olet_nyt_tassa_x)   # TODO
        
        print("\navaimet_eri_kerros", avaimet_eri_kerros)
        data[olet_nyt_tassa_y][olet_nyt_tassa_x] = "."
        if len(avaimet_eri_kerros) == 2:
            loytyi_2_avainta(avaimet_eri_kerros, askeleet)
        else:
            for avain in avaimet_eri_kerros:
                etsi_kirjainpari(avain)
                askeleet += avaimet_eri_kerros[avain]
                data[olet_nyt_tassa_y][olet_nyt_tassa_x] = "."
                print(data[1])
                print(data[3])
        print("askeleet", askeleet)



readfile()
print(data[1])
main()

