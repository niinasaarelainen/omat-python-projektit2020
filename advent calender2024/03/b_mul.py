import re

data = []
tulos = 0
enabled = True   # do()    or     don't()


"""   oikein: mul(44,46)  """
"""   väärin: mul(4*      mul(6,9!    ?(12,34)    mul ( 2 , 4 )   """

def readfile():
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())    


#   xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
#                       don't()                                do()    
def tutki():
    global tulos, enabled

    for rivi in data:
        tutkittava = rivi
        while "mul(" in tutkittava:
            luku = ""
            pit = 4  # mul(
            do = 100000   # joku iso luku
            dont = 100000
            start = tutkittava.index("mul(")
            etsi_tasta = tutkittava[:start][::-1]
            if ")(od" in etsi_tasta:
                do = etsi_tasta.index(")(od")
                print("do ind", do)
            if ")(t'nod" in etsi_tasta:
                dont = etsi_tasta.index(")(t'nod")
                print("dont ind", dont)
            if do < dont:
                enabled = True
            elif dont < do:
                enabled = False
                print("   False")

            #eka luku    
            while tutkittava[start + pit].isdigit():
                luku += tutkittava[start + pit]
                pit += 1
            if luku != "":
                luku1 = int(luku)
                print(luku1)
            else:
                tutkittava = tutkittava[start + 1:] 
                continue

            if tutkittava[start + pit] == ",":
                pit += 1
                luku = ""
            else:
                tutkittava = tutkittava[start + 1:] 
                continue            

            while tutkittava[start + pit].isdigit():
                luku += tutkittava[start + pit]
                pit += 1
            if luku != "":
                luku2 = int(luku)
                print(luku2)
            else:
                tutkittava = tutkittava[start + 1 + pit:] 
                continue

            if tutkittava[start + pit  ] == ")":
                print(")")
                tutkittava = tutkittava[start + pit :] 
            else:
                tutkittava = tutkittava[start + pit :] 
                continue
            
            if enabled:
                tulos += luku1 * luku2
            
            print(" tulos lopussa", tulos)




readfile()
tutki()
print(tulos)