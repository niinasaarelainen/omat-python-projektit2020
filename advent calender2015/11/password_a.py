passw = "hepxcrrz"   # oikea
passw = "abcdefgh"
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
    for i in range(len(str)-1, 0, -1):
        vika = str[i]
        while ord(vika) < 122:
            nro = ord(vika) + 1
            if nro == 123:
                l[i-1] = chr(ord(str[i-1])+1)
            else:
                l[i] = chr(nro)
            str = "".join(l)
            tulos = increasing_straight(str) and kielletyt_kirjaimet(str) and double_letters(str)
            if tulos:
                print(str)
            vika = str[i]




increment(passw)
print(increasing_straight(passw))
print(kielletyt_kirjaimet(passw))
print(double_letters(passw))
tulos = increasing_straight(passw) and kielletyt_kirjaimet(passw) and double_letters(passw)
print(passw, tulos)