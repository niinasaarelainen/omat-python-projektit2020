data = []

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())   


def vertaa(luvut, pos):
    for i in range(len(luvut) -1):
        if pos:
            print(int(luvut[i]) - int(luvut[i+1]))
            if int(luvut[i]) - int(luvut[i+1]) not in [1,2,3]:
                return 0
        else:
            if int(luvut[i]) - int(luvut[i+1]) not in [-1,-2,-3]:
                return 0

    return 1


def lue():
    safe = 0

    for rivi in data:
        print("safe", safe)
        luvut = rivi.split(" ")
        verrokki = int(int(luvut[0]) - int(luvut[1]))
        print("verrooki", verrokki)
        if verrokki in [1,2,3]:
            print("pos")
            pos = True
            safe += vertaa(luvut, pos)
        elif verrokki in [-1,-2,-3]:
            pos = False  
            safe += vertaa(luvut, pos)  

    print("safe", safe)    


readfile() 
lue()
