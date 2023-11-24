
data = []
sum = 0

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:        
        data.append(rivi.strip())


def lue():
    global sum
    for rivi in data:
        kerataan_numeroa = []
        for k in rivi:
            if k == "-":
                kerataan_numeroa.append(k)
            elif k.isdigit():
                kerataan_numeroa.append(k) 
            elif kerataan_numeroa != []:
                nro = "".join(kerataan_numeroa)
                sum += int(nro)
                kerataan_numeroa = []    


readfile()
lue()
print(sum)