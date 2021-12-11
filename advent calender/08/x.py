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
vastaavuudet = {"a": None, "b":  None, "c": None, "d": None, "e": None, "f": None, "g": None }
pituudet = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
x_kpl_kirjainta = []


def readfile():   # a-kohta
    global output_values
    f = open("data.txt", "r")         
    for rivi in f:
        alut_ja_loput.append(rivi.split(" | "))
    print(alut_ja_loput)
    for i in range(len(alut_ja_loput)):
        output_values.append(alut_ja_loput[i][1].split(" "))
    print()
    print(output_values)
    
    

def montako_1478():
    global vastaus
    for lista in output_values:
        for str in lista:
            if len(str.strip()) in [2, 3, 4, 7]:
                vastaus += 1
    print(vastaus)


def readfile2():   # a-kohta    
    global output_values
    f = open("data_rivi.txt", "r")         
    for rivi in f:
        alut_ja_loput.append(rivi.split(" | "))
    print("alut_ja_loput", alut_ja_loput)
    for i in range(len(alut_ja_loput)):
        output_values.append(alut_ja_loput[i][0].split(" "))
        output_values.append(alut_ja_loput[i][1].split(" "))
    print()
    print("output_values", output_values)
    

def muodosta_x_kpl_kirjainta():
    global x_kpl_kirjainta, pituudet
    temp_kaikki_erilaiset_kerran = []
    for lista in output_values:
        print("lista", lista)
        for str in lista:
            if sorted(str.strip()) not in temp_kaikki_erilaiset_kerran:
                temp_kaikki_erilaiset_kerran.append(sorted(str.strip()))

    for item in temp_kaikki_erilaiset_kerran:
        pituudet[len(item)] += [item]

    for montako, kirjainsarjat in pituudet.items():
        for sarja in kirjainsarjat:
            for kirjain in sarja:
                for item in  pituudet[2]:
                    if len(sarja) == 3 and kirjain not in item:
                        vastaavuudet["a"] = kirjain
    print(vastaavuudet)



def b_kohta():
    readfile2()
    muodosta_x_kpl_kirjainta()


#readfile()
#montako_1478()

b_kohta()