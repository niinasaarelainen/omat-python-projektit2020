
data_orig = ""



def readfile():
    global data_orig
    f = open("data.txt", "r") 
    for rivi in f:
        data_orig = rivi.strip()


def react(rivi):
    uusi_lista = []
    uusi_rivi = ""
    
    
    
    for i in range(len(rivi) - 1):
        uusi_lista = list(rivi[:i + 1])   # ei koko listaa, test data2:ensin oikea tulos vanh. metodilla muistiin
        pari = [rivi[i], rivi[i + 1]]
        lower =  [item for item in pari if item.islower()]
        if len(lower) == 1 and rivi[i].lower() == rivi[i + 1].lower():
            uusi_lista[i] = ""
            uusi_lista[i + 1] = ""
            uusi_rivi = "".join(uusi_lista)
            break  

    
    if uusi_rivi != rivi:
        print(uusi_rivi)
        react(uusi_rivi)        

    


readfile()
react(data_orig) 
 