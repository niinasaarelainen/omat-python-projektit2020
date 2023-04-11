
data = []  
rekisterit = {}
recovered_frequency = 0


def readfile():
    f = open( "data_a.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        data.append(rivi)


def luo_rekisterit():
    for rivi in data:   # mod a 5    snd a
        sp = rivi.split(" ")
        rek = sp[1]
        rekisterit[rek] = 0

def tutki_3_parametriset(kasky, rek, maara):
    if kasky == "set":
        rekisterit[rek] = maara
    elif kasky == "add":
        rekisterit[rek] += maara
    elif kasky == "mul":
        rekisterit[rek] *= maara
    elif kasky == "mod":
        rekisterit[rek] % maara
    elif


def kay_lapi():
    missa_mennaan = 0
    while True:       # mod a 5    snd a
        sp = data[missa_mennaan].split(" ")
        kasky = sp[0]        
        rek = sp[1]

        if kasky == "snd":
            pass

        if kasky == "rcv":
            pass

        if len(sp) > 2:  # muut paitsi snd ja rcv
            maara = sp[2]
            #jump
            if kasky == "jgz":
                if rekisterit[rek] > 0:
                    missa_mennaan += maara
            else:
                tutki_3_parametriset(kasky, rek, maara)



readfile()
luo_rekisterit() 
print(rekisterit)
kay_lapi()


