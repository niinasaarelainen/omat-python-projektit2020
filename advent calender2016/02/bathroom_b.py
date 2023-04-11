
data = []
numerot = ['0','0','1','0','0'], ['0','2','3','4','0'], ['5','6','7','8','9'], ['0','A','B','C','0'], ['0','0','D','0','0']
koodit = []

"""
    1
  2 3 4
5 6 7 8 9
  A B C
    D     """



def readfile():
    f = open("data.txt", "r")   # ULRD
    for rivi in f:
        data.append(rivi.strip())


def x():
    
    rivi = 2
    sarake = 0   # aloitus 5:sta

    for r in data:   
        print(r)    
        for kirjain in r:
            if kirjain == "U":                
                rivi = max(0, rivi - 1)
                if numerot[rivi][sarake] == '0':
                    rivi += 1
            if kirjain == "D":
                rivi = min(4, rivi + 1)
                if numerot[rivi][sarake] == '0':
                    rivi -= 1
            if kirjain == "R":
                sarake = min(4, sarake + 1)
                if numerot[rivi][sarake] == '0':
                    sarake -= 1
            if kirjain == "L":
                sarake = max(0, sarake - 1)
                if numerot[rivi][sarake] == '0':
                    sarake += 1
            print(rivi, sarake)
        koodit.append(numerot[rivi][sarake])

    


readfile()
print(x())

a = map(str, koodit)    
print(''.join(a))
 
