data = []
sum = 0
object_alkaa = False
red = []
onko_red = False
numerot_talteen = []

def readfile():
    f = open("data_1.txt", "r") 
    for rivi in f:        
        data.append(rivi.strip())


def lue():
    global sum, object_alkaa, onko_red, numerot_talteen
    for rivi in data:
        kerataan_numeroa = []
        for k in rivi:
            if k == "{":
                object_alkaa = True
            elif k == "}":
                if not onko_red:
                    for nro in numerot_talteen:
                        sum += int(nro)
                numerot_talteen = []
                object_alkaa = False
                onko_red = False
            elif k == "r":
                red.append(k)
            elif k == "e" and red != [] and red[0] == "r":
                red.append(k)
            elif k == "d" and red[0] == "r" and red[1] == "e":
                onko_red = True
            elif k == "-":
                kerataan_numeroa.append(k)
            elif k.isdigit():
                kerataan_numeroa.append(k) 
            elif kerataan_numeroa != []:
                nro = "".join(kerataan_numeroa)
                if object_alkaa:
                    numerot_talteen.append(int(nro))
                else:
                    sum += int(nro)
                kerataan_numeroa = []    

        print(sum)


readfile()
lue()
#print(sum) # 50609 too low