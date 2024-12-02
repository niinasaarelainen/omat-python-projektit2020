data = []
unsafe = []
safe = 0
safe_or_uns = []

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())   


def vertaa(luvut, pos):
    global unsafe
    for i in range(len(luvut) -1):
        if pos:
            if int(luvut[i]) - int(luvut[i+1]) not in [1,2,3]:
                unsafe.append(luvut)
                return 0       
        else:
            if int(luvut[i]) - int(luvut[i+1]) not in [-1,-2,-3]:
                unsafe.append(luvut)
                return 0
    return 1         


def vertaa2(luvut, pos):   # !!!!!!!
    global safe
    ongelmat = []
    for i in range(len(luvut) -1):
        
        if pos:
            if int(luvut[i]) - int(luvut[i+1]) not in [1,2,3]:
                ongelmat.append(i)
        else:
            if int(luvut[i]) - int(luvut[i+1]) not in [-1,-2,-3]:
                ongelmat.append(i)

    if len(ongelmat) <= 1:
        print("ongelmat", ongelmat, luvut)
        if len(luvut) - ongelmat[0] == 2: # toka vika ainoa ongelma, eli poistamalla vika ok !!
            safe += 1
        else:
            fix(ongelmat[0], luvut, pos)


def fix(ind, luvut, pos):
    global safe
    if pos:
        print("  FIX", int(luvut[ind-1]) - int(luvut[ind+1]))
        if int(luvut[ind-1]) - int(luvut[ind+1]) not in [1,2,3]:
            print("   fail")
        else:
            safe += 1
    else:
        if int(luvut[ind -1]) - int(luvut[ind+1]) not in [-1,-2,-3]:
            print("   fail")
        else:
            safe += 1



def lue():
    global safe, unsafe

    for rivi in data:
        luvut = rivi.split(" ")
        verrokki = int(int(luvut[0]) - int(luvut[1]))
        if verrokki in [1,2,3]:
            pos = True
            safe += vertaa(luvut, pos)
        elif verrokki in [-1,-2,-3]:
            pos = False  
            safe += vertaa(luvut, pos)   #TODO  poista eka alkio ja tutki loput
        else:
            print("  luvut[1:]", luvut[1:])
            safe_or_uns.append(luvut[1:])


def lue_array(a):
    global safe

    for rivi in a:
        verrokki = int(rivi[0]) - int(rivi[1])
        if verrokki in [1,2,3]:
            pos = True
            safe += vertaa(rivi, pos)
        elif verrokki in [-1,-2,-3]:
            pos = False  
            safe += vertaa(rivi, pos)   


def korjaa(unsafe):
    global safe
    for rivi in unsafe:
        verrokki = int(int(rivi[0]) - int(rivi[1]))
        print("verrooki", verrokki)
        if verrokki in [1,2,3]:
            pos = True
            vertaa2(rivi, pos)
        elif verrokki in [-1,-2,-3]:
            pos = False  
            vertaa2(rivi, pos)  

    


readfile() 
lue()
print(unsafe)
print("safe ennen korjaa-unsafe", safe)    
korjaa(unsafe)
print("safe ennen korjaa-safe_or_uns", safe)    
lue_array(safe_or_uns)
print("safe jälkeen korjaa", safe)     #548, 558 too low   566
