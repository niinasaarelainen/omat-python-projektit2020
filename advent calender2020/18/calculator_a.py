data = []
lopputulokset = []

def readfile():   # a-kohta
    global data
    f = open("data.txt", "r")         
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
    vastaukset = []      # tänne aina uusi rivi
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

        rivi = vastaukset[-1]
        print(" rivi@after - sulku-for", rivi)
        tulos = int(rivi[0])
        for i in range(len(rivi)-1):
            if rivi[i + 1] in ["(", ")"]:
                pass
            elif rivi[i] == "+":
                tulos += int(rivi[i + 1])  
            elif rivi[i] == "*":
                tulos *=  int(rivi[i + 1]) 

            print(tulos)
            

        print("**tulos", tulos)     # 12240
        lopputulokset.append(tulos)



def suluissa(rivi, alku, loppu):
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
