"""

0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg


 0: a- g, paitsi d  =6kpl   
 1: c, f            =2kpl
 2: a, c, d, e, g   =5kpl   
 3: a, c, d, f, g   =5kpl  
 4: b, c, d, f      =4kpl
 5: a, b, d, f, g   =5kpl    
 6: a- g, paitsi c  =6kpl   
 7: a, c, f         =3kpl
 8: a - g           =7kpl
 9: a- g, paitsi e  =6kpl   

2 kirjainta : "1"   HELPOIN MUOTO ( c ja f, kumpi on kumpi ??)
3 kirjainta : "7"    7 = 1+a
4 kirjainta : "4"    4= 1+ b ja d
5 kirjainta : "2", "3", "5"    2 ainoa jossa ei f
6 kirjainta : "0", "6", "9"    0= 8-d ,  6=5+e  ja 8-c , 9 = 8-e
7 kirjainta : "8"

"""

alut_ja_loput = []
output_values = []
vastaus = 0
pituudet = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

def readfile():   # a-kohta
    global output_values
    f = open("data.txt", "r")         
    for rivi in f:
        alut_ja_loput.append(rivi.split(" | "))
    print(alut_ja_loput)
    for i in range(len(alut_ja_loput)):
        output_values.append(alut_ja_loput[i][0].split(" "))
        output_values.append(alut_ja_loput[i][1].split(" "))
    print()
    print("output_values", output_values)
    
    
    

def montako_1478():
    global vastaus
    for lista in output_values:
        for str in lista:
            if len(str.strip()) in [2, 3, 4, 7]:
                vastaus += 1
    print(vastaus)


def readfile2():   # b-kohta    
    global output_values
    f = open("data_easy.txt", "r")         
    for rivi in f:
        alut_ja_loput.append(rivi.split(" | "))
    print("alut_ja_loput", alut_ja_loput)
    

def muodosta_x_kpl_kirjainta():
    global pituudet, output_values

    print()
    print("output_values", output_values)
    for str in output_values[0]:
        pituudet[len(str)].append(str)

    oikeat_vastaukset = [-1,-1,-1,-1, -1,-1, -1,-1, -1,-1]
    oikeat_vastaukset[1] = pituudet[2][0]
    oikeat_vastaukset[7] = pituudet[3][0]
    oikeat_vastaukset[4] = pituudet[4][0]
    oikeat_vastaukset[8] = pituudet[7][0]

    # "2" ainoa jossa ei f, eli ainoa jossa count(x) == 9
    for kirjain in "abcdefg":
        montako = 0
        str_talteet = ""
        vastaus = ""
        for val in pituudet.values():
            for str in val:
                if kirjain in str:
                    montako += 1
                else:
                    str_talteet = str
                    #print(str_talteet)
        #print(kirjain, montako, str_talteet)
        if montako == 9 and str_talteet != "":
            vastaus = str_talteet
            break
    print("vastaus", vastaus)
    oikeat_vastaukset[2] = vastaus
    #print("pituudet[5]", pituudet[5])
    pituudet[5].remove(vastaus)


    for str in pituudet[6]:
        etsittava = set(pituudet[2][0])
        #if etsittava.issubset(set(str)):
        #    print(" TESTIMOI")
        if not etsittava.issubset(set(str)):
            #print("    kutosen etsintaä:  ", etsittava, "not in set", set(str))
            oikeat_vastaukset[6] = str
            pituudet[6].remove(str)
    
    
    for str in pituudet[5]:
        etsittava = set(oikeat_vastaukset[6])
        print("    vitosen etsintaä:   set(str), etsittava", set(str), etsittava)
        if set(str).issubset(etsittava):
            oikeat_vastaukset[5] = str 
            pituudet[5].remove(str)

    oikeat_vastaukset[3] = pituudet[5][0]   # vain yksi jäljellä

    for str in pituudet[6]:
        etsittava = set(pituudet[4][0])
        if etsittava.issubset(set(str)):
            print(etsittava, "issubset", set(str))
            oikeat_vastaukset[9] = str
            pituudet[6].remove(str)
            oikeat_vastaukset[0] = pituudet[6][0]

    
    return oikeat_vastaukset
            

def vastaus(oikeat_vastaukset):
    vastaus = ""
    print(oikeat_vastaukset)
    for value in output_values[1]:
        value = value.strip()
        print("value ", value)
        for i in range(len(oikeat_vastaukset)):
            
            if set(oikeat_vastaukset[i]) == set(value):
                vastaus += str(i)
    print(vastaus)



def b_kohta():
    global output_values
    readfile2()   

    
    for i in range(len(alut_ja_loput)):
            output_values = []
            output_values.append(alut_ja_loput[i][0].split(" "))
            print("alut_ja_loput[i][0]", alut_ja_loput[i][0])
            output_values.append(alut_ja_loput[i][1].split(" ")) 
            print("alut_ja_loput[i][1]", alut_ja_loput[i][1])
            print("output_values", output_values)
            vastaus(muodosta_x_kpl_kirjainta())


#readfile()
#montako_1478()

b_kohta()