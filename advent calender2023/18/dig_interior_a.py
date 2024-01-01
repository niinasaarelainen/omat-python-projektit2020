import re

data = []  
tulos = 0
x_max = 0   
y_max = 0
x_min = 0   
y_min = 0
kuva = []


def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip().split(" "))


def selvita_dimensiot():
    global x_max, y_max, x_min, y_min
    x = 1    
    y = 1    
    for rivi in data:
        # oikea - vasen:
        if rivi[0] == 'R':
            x += int(rivi[1])
            x_max = max(x, x_max)
        if rivi[0] == 'L':
            x -= int(rivi[1])
            x_min = min(x, x_min)

        # alas - ylös:
        if rivi[0] == 'D':
            y += int(rivi[1])
            y_max = max(y, y_max)
        if rivi[0] == 'U':
            y -= int(rivi[1])
            y_min = min(y, y_min)

    

def rakenna_tyhja_kuva():
    global kuva
    for y in range(y_max - y_min):
        rivi = []
        for x in range(x_max - x_min):
            rivi.append('.')
            
        kuva.append(list(rivi))


def rakenna_hashtag():
    x = abs(x_min)
    y = abs(y_min)
    kuva[y][x] = "#"  # aloituskohta 

    for suunta, montako, ihansama in data:
        if suunta == 'R':
            for x_apu in range(int(montako) ):
                x += 1
                kuva[y][x] = "#"
        if suunta == 'L':
            for x_apu in range(int(montako) ):
                x -= 1
                kuva[y][x] = "#"
        if suunta == 'D':
            for y_apu in range(int(montako) ):
                y += 1
                kuva[y][x] = "#"
        if suunta == 'U':
            for y_apu in range(int(montako) ):
                y -= 1
                kuva[y][x] = "#"


def tutki_vain2():
    global tulos
    monesko_rivi = 0
    for rivi in kuva:
        rivi = "".join(rivi)
        if '.' not in rivi:
            tulos += len(rivi)
        else:
            alku = rivi.index('#')        
            loppu = rivi.rfind('#')
            nyt_lisataan =  loppu - alku + 1
            tulos += nyt_lisataan

        print(monesko_rivi, nyt_lisataan)
        monesko_rivi += 1

def tutki():
    global tulos
    monesko_rivi = 0
    
    for rivi in kuva:
        loppu_ind_saato = 0  # ei saa olla ennen alkua
        rivi = "".join(rivi)
        print(rivi)
        if '.' not in rivi:
            tulos += len(rivi)
        else:
            alut = [m.start() for m in re.finditer(r"#\.",rivi)]   # REgular Exp !!!!!!!!!!!!
            loput = [m.start() for m in re.finditer(r"\.#",rivi)]   # REgular Exp !!!!!!!!!!!!
            
            for ind in range(0, len(alut), 2):                
                if loput[ind] < alut[ind] :
                    loppu_ind_saato += 1
                if ind + loppu_ind_saato < len(loput):
                    nyt_lisataan = loput[ind + loppu_ind_saato] - alut[ind]  # vain pisteet
                    tulos += nyt_lisataan
                    print(monesko_rivi, nyt_lisataan, alut, loput)

            tulos += rivi.count("#")     
            
            
        monesko_rivi += 1
        


readfile()
selvita_dimensiot()
#print(x_max, "x_max")
#print(y_max, "y_max")
rakenna_tyhja_kuva()
rakenna_hashtag()

"""
str = "".join(kuva[127])
loput = [m.start() for m in re.finditer(r"\.#",str)]   # REgular Exp !!!!!!!!!!!!
for ind in range(0, len(loput), 2):
    print(loput[ind]) 
print(loput)"""
tutki()
#tulos = 0
#tutki_vain2()
print(tulos)   # 73421  too high, 68999, 50071 
#print(x_min, y_min, x_max, y_max)

