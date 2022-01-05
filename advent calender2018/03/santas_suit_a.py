import math

claims = []
matriisi = []
matriisin_koko = 1000

"""
#123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 
2 inches from the top edge, 5 inches wide, and 4 inches tall.  """

def readfile():
    f = open("data.txt", "r")    # #1 @ 335,861: 14x10
    for rivi in f:
        sp = rivi.strip().split(" @ ")
        claims.append(sp[1])
    print(claims)


def alusta_matriisi():
    for i in range(matriisin_koko):
        matriisi.append([])
        for j in range(matriisin_koko):
            matriisi[-1].append(".")



def jatkokasittele():
    global claims, matriisi
    for rivi in claims:
        sp = rivi.split(": ")
        sp2 = sp[0].split(",")
        from_left_edge = int(sp2[0])
        from_top_edge = int(sp2[1])
        sp3 = sp[1].split("x")
        wide = int(sp3[0])
        tall = int(sp3[1])
        for w in range(wide):
            for t in range(tall):
                if matriisi[from_top_edge + t][from_left_edge + w] == ".":
                    matriisi[from_top_edge + t][from_left_edge + w] = 1
                else:
                    matriisi[from_top_edge + t][from_left_edge + w] += 1
    

def laske_useat():
    monta = 0
    for rivi in range(matriisin_koko):   
        for c in range(matriisin_koko):
            if matriisi[rivi][c] != ".":
                if matriisi[rivi][c] > 1:
                    monta +=1

    return monta


readfile()
alusta_matriisi()
jatkokasittele()
"""
for rivi in matriisi:
    print(rivi)"""
print(laske_useat())