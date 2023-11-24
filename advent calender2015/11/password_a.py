passw = "hepxcrrz"   # oikea
passw = "hepxxyzz"
#passw = "vvxzzabc"   # ok
#passw = "abbcegjk"
passw_uusi = ""
data = []





def increasing_straight(str):
    edellinen = '0'
    suora = 1
    for c in str:
        if ord(c) == ord(edellinen) + 1:
            suora += 1
            if suora == 3:
                return True
        else:
            suora = 1
        edellinen = c

def kielletyt_kirjaimet(str):
    if "i" in str or "o" in str or "l" in str:
        return False
    return True

def double_letters(str):
    edellinen = ""
    pareja = 0
    for c in str:
        if c == edellinen:
            pareja += 1
            edellinen = ""
        else:
            edellinen = c
    if pareja >= 2:
        return True

 


def increment(str):
    l = list(str)
    test_counter = 0
    ind = len(str) - 1
    while True:        
        skrollataan = str[ind]        
        while  test_counter < 11111970:
            nro = ord(skrollataan) + 1
            skrollataan = chr(nro)
            ind_temp = ind
            if  nro == 123:
                while nro == 123:   # 122 = z  
                    nro = ord(str[ind_temp-1])+1
                    if nro == 123:
                        l[ind_temp-1] = 'a' 
                    else: 
                        l[ind_temp-1] = chr(nro)
                    l[ind_temp] = 'a' 
                    skrollataan = "a"
                    ind_temp -= 1
            else:
                l[ind] = chr(nro)
            str = "".join(l)
            tulos = increasing_straight(str) and kielletyt_kirjaimet(str) and double_letters(str)
            #print(str)
            if tulos:
                print(str, "jee")
                return
            test_counter += 1            
            
        ind -= 1
            





increment(passw)
"""
print(increasing_straight(passw))
print(kielletyt_kirjaimet(passw))
print(double_letters(passw))
tulos = increasing_straight(passw) and kielletyt_kirjaimet(passw) and double_letters(passw)
print(passw, tulos) """
print(chr(122))