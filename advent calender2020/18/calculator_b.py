data = []
vastaukset = []
lopputulokset = []

def readfile():   # a-kohta
    global data
    f = open("data_sulut.txt", "r")         
    for rivi in f:
        rivi = rivi.replace("(", " ( ")
        rivi = rivi.replace(")", " ) ")
        rivi = rivi.replace("  ", " ")    # 2 tyhjää pois
        data.append(rivi.strip().split(" "))
    print(data)


def maarita_alkusulut(rivi):    
    alkusulut = []
    for i in range(len(rivi) ):
        if "(" in rivi[i]:     
            alkusulut.append(i)

    return alkusulut



def calculate():    
    global vastaukset 
    for rivi_ind in range(len(data)):
        vastaukset.append(data[rivi_ind])
        alkusulut = maarita_alkusulut(data[rivi_ind])  
        for alkusulku in reversed(alkusulut):
            rivi = vastaukset[-1]
            #print("rivi@sulku-for", rivi)
            loppusulku = (rivi[alkusulku:]).index(")") + alkusulku
            #print("loppusulku", loppusulku)
            sulku_tulos = suluissa(rivi, alkusulku, loppusulku)            
            vastaukset.append(rivi[:alkusulku] + [sulku_tulos] + rivi[loppusulku + 1:])
            #print(" !!", rivi[loppusulku + 1:], loppusulku)

        plussaa(vastaukset[-1] )    

        tulos = tulo(vastaukset[-1])            

        print("**tulos", tulos)    
        #lopputulokset.append(tulos)


def plussaa(rivi):
    global vastaukset
    while "+" in rivi:
        #for times in range(3):
            plussa_ind = rivi.index("+")
            
            plussa_tulos = int(rivi[plussa_ind - 1]) + int(rivi[plussa_ind + 1])
            loppuosa = []
            if plussa_ind + 1 < len(rivi) - 1:
                loppuosa = rivi[plussa_ind + 2:]
            #print("plussa_tulos", plussa_tulos)
            vastaukset.append(rivi[:max(0, plussa_ind - 1)] + [plussa_tulos] +loppuosa)
            rivi = vastaukset[-1]
            print(" plussssa", rivi, plussa_ind)


def tulo(rivi):
    print(rivi)
    vastaus = 1
    for item in rivi:
        if item != "*":
            vastaus *= int(item)
            print(vastaus)

    return vastaus



def suluissa(rivi, alku, loppu):    # TODO  täältä kutsutaan  plussaa()
    print(" alku ", alku)
    while rivi[alku + 1]  in ["(", ")"]:
        alku += 1

    tulos = int(rivi[alku + 1])
    for i in range(alku+1, loppu):
        if rivi[i + 1] in ["(", ")"]:
            break
        elif rivi[i] == "+":
            tulos += int(rivi[i + 1])  
        elif rivi[i] == "*":
            tulos *=  int(rivi[i + 1])  

        #print("  välitulos", tulos) 

    return tulos



readfile()
calculate()  
print()
print(len(lopputulokset))
print(sum(lopputulokset))    # 25391626929  too low
                             # 98621258158412
