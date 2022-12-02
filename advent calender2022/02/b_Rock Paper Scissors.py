data = []

"""opponen:
   A for Rock
   B for Paper
   C for Scissors

   me:
   X means you need to lose, 
   Y means you need to end the round in a draw
   Z means you need to win

   0  lost,  3 draw,  6 won
"""

def readfile():
    data = []
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip().split(" "))
    
    return data


def muunna(a):
    rpc = ["A", "B", "C"]
    pisteet_voittoko = {"X" : 0, "Y" : 3, "Z": 6}
    score = 0
    for rivi in a:
        ind = rpc.index(rivi[0])
        if rivi[1] == "X":
            score += (ind + 2) % 3 + 1   # +1 = indeksissä 0 on 1 piste
        elif rivi[1] == "Y":
            score += ind + 1
        elif rivi[1] == "Z":
            score += (ind + 1) % 3 + 1
        score += pisteet_voittoko[rivi[1]]
    
    return score



readfile() 
print(muunna(readfile()))
