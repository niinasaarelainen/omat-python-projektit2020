data = []
luvut = 0
sums1 = []
sums2 = []


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
        for ind in range(len(rivi)):
            if rivi[ind].isdigit():
                print("oli digit")
                digits.append(rivi[ind])
            elif rivi[ind] in aloituskirjaimet:
                #alkaa oikealla kirjaimella:
                hitit = [sana for sana in luvut_kirj if sana[0] == rivi[ind]]
                for hit in hitit:
                    if hit == rivi[ind: min(ind + len(hit), len(rivi))]:
                        digits.append(luvut_kirj[hit]) 
            print("digits", digits)

        #print(digits)
        luku = int(digits[0] + digits[-1])
        #print(luku)
        sums1.append(luku)
        luvut += luku


def summat2():    # huom ! index-metodi antaa vain 1. okkurenssin !!!! älä käytä, rivi  "two1two" ei toimi
    global luvut
    luvut = 0
    luvut_kirj = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
 
    for rivi in data:   
        hitit = []
        for key in luvut_kirj:
            results = [i for i in range(len(rivi)) if rivi.startswith(key, i)] 
            for ind in results:
                hitit.append([luvut_kirj[key], ind])
            for ind in range(len(rivi)):
                if rivi[ind].isdigit():
                    hitit.append([rivi[ind], ind])
           
        
        hitit.sort(key=lambda x: x[1])
        print(hitit)
        luku = int(hitit[0][0] + hitit[-1][0])
        #print(luku)
        sums2.append(luku)
        luvut += luku




readfile()
summat()                # 281  ,  54530
summat2()   
print(len(sums1), len(sums2))


for i in range(0, 1000):
    if sums1[i] != sums2[i]:
        print(i, sums1[i], sums2[i])  

print(luvut)