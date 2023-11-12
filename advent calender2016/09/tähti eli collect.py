
data = []


def readfile():
    f = open("tähti.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def tutki_collect():

    for rivi in data: 
        sana, *numerot = rivi.split("X")  # jos syöte vain 1 numero, menee se sana-muuttujaan !!
        numerot = [int(n) for n in numerot]
        print(sana, numerot)

               
def tutki_kaikki():
    for rivi in data:     
        kaikki = rivi.split("X")  
        ####   if  else   
        kaikki_muunnettuna = [int(n) if n.isdigit() else n for n in kaikki]

        #### pelkkä if, huomaa if:n paikka yllä ja alla 
        numerot = [int(n) for n in kaikki  if n.isdigit() ]
        print(kaikki_muunnettuna, numerot)


readfile()
tutki_kaikki()
tutki_collect()
