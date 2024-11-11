
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


def calculate():
    global data
    
    vastaukset = []      # tänne aina uusi rivi
    for rivi in range(len(data)):
        tulos = int(data[rivi][0])
        alkusulut = []
        loppusulut = []
        suluton_data = []
        for i in range(len(data[rivi]) ):
            if "(" in data[rivi][i]:     
                alkusulut.append(i)
            elif ")" in  data[rivi][i]:
                loppusulut.append(i)
            else: 
                suluton_data.append(data[rivi][i])

        print(alkusulut, loppusulut, suluton_data)   # sulkujen indeksit eivät päde suluton_data:an
        
        alkuind = -1
        for loppusulku in loppusulut:
            sulku_tulos = suluissa(data[rivi], alkusulut[alkuind], loppusulku)            
            vastaukset.append(data[rivi][:alkusulut[alkuind]] + [sulku_tulos] + data[rivi][loppusulku:])
            alkuind -= 1
            print("vastaukset", vastaukset)

        rivi = vastaukset[-1]
        for i in range(len(rivi)-1):
            if rivi[i + 1] in ["(", ")"]:
                pass
            elif rivi[i] == "+":
                tulos += int(rivi[i + 1])  
            elif rivi[i] == "*":
                tulos *=  int(rivi[i + 1]) 
            

        print("**tulos", tulos)



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
