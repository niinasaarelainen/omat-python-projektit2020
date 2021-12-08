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

2 kirjainta : "1"   HELPOIN MUOTO
3 kirjainta : "7"   2. HELPOIN MUOTO --> EI YLÄRIVIÄ = 4 (ykkönen jo selvitetty)
4 kirjainta : "4"
5 kirjainta : "2", "3", "5"
6 kirjainta : "0", "6", "9"
7 kirjainta : "8"

"""

alut_ja_loput = []
output_values = []
vastaus = 0


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



readfile()
montako_1478()