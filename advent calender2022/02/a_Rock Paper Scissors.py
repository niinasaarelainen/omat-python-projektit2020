data = []

"""opponen:
   A for Rock
   B for Paper
   C for Scissors

   me:
   X for Rock  1
   Y for Paper  2
   Z for Scissors  3

   0  lost,  3 draw,  6 won
"""

def readfile():
    data = []
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip().split(" "))
    
    return data

#tapa1, eihyvä, aluksi luulin että -1 riittää
def muunna(a):  # 11386
    m = {"A" : 0, "B" : 1, "C" : -1, "X" : 0, "Y" : 1, "Z" : -1}
    pisteet_muoto = {"X" : 1, "Y" : 2, "Z": 3}
    pisteet_voitto = {-1 : 6, 0 : 3, 1: 0, 2: 6, -2: 0}
    score = 0
    for rivi in a:
        kamppailu = m[rivi[0]] - m[rivi[1]]
        print(m[rivi[0]],  m[rivi[1]])
        print(kamppailu)
        score += pisteet_voitto[kamppailu]
        score += pisteet_muoto[rivi[1]]
    
    return score

#tapa12
def muunna2(a):  # 11386
    rpc1 = ["A", "B", "C"]
    rpc2 = ["X", "Y", "Z"]
    score = 0
    for rivi in a:
        ind1 = rpc1.index(rivi[0])
        ind2 = rpc2.index(rivi[1])
        if ind1-ind2 == -1 or ind1-ind2 == 2:
            score += 6
        elif ind1-ind2 == 0:
            score += 3          # häviö = 0, joten elseä ei tarvita
        
        score += ind2 + 1  # muoto
    
    return score



readfile() 
print(muunna2(readfile()))
