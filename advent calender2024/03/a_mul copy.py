data = []
tulos = 0


"""   oikein: mul(44,46)  """
"""   väärin: mul(4*      mul(6,9!    ?(12,34)    mul ( 2 , 4 )   """

def readfile():
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())    


#   xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
def tutki():
    global tulos

    for rivi in data:
        tutkittava = rivi
        while "mul(" in tutkittava:
            luku = ""
            pit = 4  # mul(
            start = tutkittava.index("mul(")
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
            
            tulos += luku1 * luku2
            print(tulos)




readfile()
tutki()
print(tulos)