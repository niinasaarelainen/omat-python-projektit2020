data = []
sum = 0
object_alkaa = False
onko_red = False

red = []
numerot_talteen = []
aalto_pino = []

def readfile():
    f = open("data .txt", "r") 
    for rivi in f:        
        data.append(rivi.strip())


def lue_eired():
    global sum, object_alkaa, onko_red, numerot_talteen
    pop_count = 0
    for rivi in data:
        kerataan_numeroa = []
        for k in rivi:
            #print(k, onko_red)
            if k == "{":
                object_alkaa = True
                aalto_pino.append(numerot_talteen)
                #print("aalto_pino", aalto_pino)
                numerot_talteen = []

            elif k == "}":
                print("numerot_talteen", numerot_talteen)
                if numerot_talteen != []:
                    for nro in numerot_talteen:  # aiemmat kerätyt
                        sum += int(nro)
                    if kerataan_numeroa != []:
                        nro = "".join(kerataan_numeroa) # nykyinen ei ole vielä talletettu numerot_talteen:een
                        sum += int(nro)
                else: #  numerot_talteen on tyhjä
                    #print("aalto_pino", aalto_pino)
                    numerot = aalto_pino.pop()
                    pop_count += 1
                    for nro in numerot: 
                        sum += int(nro)
                
                kerataan_numeroa = [] 
                numerot_talteen = []                
                object_alkaa = False
                onko_red = False

            elif k == "r":
                red.append(k)

            elif k == "e" and red != [] and red[0] == "r":
                red.append(k)

            elif k == "d" and red != [] and red[0] == "r" and red[1] == "e":
                onko_red = True
                
            elif k == "-":
                kerataan_numeroa.append(k)
            elif k.isdigit():
                kerataan_numeroa.append(k) 

            elif kerataan_numeroa != []:
                nro = "".join(kerataan_numeroa)
                numerot_talteen.append(int(nro))                
                kerataan_numeroa = []    

        print("  sum:", sum)
        print("aalto_pino lopussa:", aalto_pino)
        print("pop_count", pop_count)

readfile()
lue_eired()
#lue()
#print(sum) # 54892 too low, ei 73910