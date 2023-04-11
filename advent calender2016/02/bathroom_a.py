
data = []
numerot = [1,2,3], [4,5,6], [7,8,9]
koodit = []



def readfile():
    f = open("data.txt", "r")   # ULRD
    for rivi in f:
        data.append(rivi.strip())


def x():
    
    rivi = 1
    sarake = 1

    for r in data:       
        for kirjain in r:
            if kirjain == "U":
                rivi = max(0, rivi - 1)
            if kirjain == "D":
                rivi = min(2, rivi + 1)
            if kirjain == "R":
                sarake = min(2, sarake + 1)
            if kirjain == "L":
                sarake = max(0, sarake - 1)
        print(rivi, sarake)
        koodit.append(numerot[rivi][sarake])

    


readfile()
print(x())

a = map(str, koodit)    
print(''.join(a))
 
