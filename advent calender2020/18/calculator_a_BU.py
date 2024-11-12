
data = []

def readfile():   # a-kohta
    global data
    f = open("data_sulut.txt", "r")         
    for rivi in f:
        rivi = rivi.replace("(", " ( ")
        rivi = rivi.replace(")", " ) ")
        rivi = rivi.replace("  ", " ")    # 2 tyhjää pois
        data.append(rivi.strip().split(" "))
    print(data)


def maarita_sulut(rivi):
    
    tulos = int(rivi[0])
    alkusulut = []
    loppusulut = []
    for i in range(len(rivi) ):
        if "(" in rivi[i]:     
            alkusulut.append(i)
        elif ")" in  rivi[i]:
            loppusulut.append(i)

    print(alkusulut, loppusulut)   # sulkujen indeksit eivät päde suluton_data:an
    return (alkusulut, loppusulut)

def calculate():
    global data
    
    vastaukset = []      # tänne aina uusi rivi
    for rivi_ind in range(len(data)):
        vastaukset.append(data[rivi_ind])
        alkusulut, loppusulut = maarita_sulut(data[rivi_ind])        
        alkuind = -1
        for loppusulku in loppusulut:   # toimii   5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
            rivi = vastaukset[-1]
            sulku_tulos = suluissa(rivi, alkusulut[alkuind], loppusulku)            
            vastaukset.append(rivi[:alkusulut[alkuind]] + [sulku_tulos] + rivi[loppusulku:])
            alkuind -= 1
            print("vastaukset", vastaukset)

        rivi = vastaukset[-1]
        tulos = int(rivi[0])
        for i in range(len(rivi)-1):
            if rivi[i + 1] in ["(", ")"]:
                pass
            elif rivi[i] == "+":
                tulos += int(rivi[i + 1])  
            elif rivi[i] == "*":
                tulos *=  int(rivi[i + 1]) 
            

        print("**tulos", tulos)     # 12240



def suluissa(rivi, alku, loppu):
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

        print("  välitulos", tulos, rivi[i]) 

    return tulos



readfile()
calculate()  
print()
