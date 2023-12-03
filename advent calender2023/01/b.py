
data = []
luvut = 0


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi)

def summat():
    global luvut
    luvut_kirj = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    aloituskirjaimet = [sana[0] for sana in luvut_kirj]
    print(aloituskirjaimet)
    for rivi in data:
        digits = []
        luku = 0
        for ind in range(len(rivi)):
            if rivi[ind].isdigit():
                digits.append(rivi[ind])
            elif rivi[ind] in aloituskirjaimet:
                hitit = [sana for sana in luvut_kirj if sana[0] == rivi[ind]]
                for hit in hitit:
                    if hit == rivi[ind: min(ind + len(hit), len(rivi))]:
                        digits.append(luvut_kirj[hit]) 

        print(digits)
        luku = int(digits[0] + digits[-1])
        print(luku)
        luvut += luku



readfile()
summat()
print(luvut)