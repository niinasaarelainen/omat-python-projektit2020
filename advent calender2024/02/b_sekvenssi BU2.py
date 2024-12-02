import copy

data = []
unsafe = []
safe = 0
safe_or_uns = []

def readfile():
    f = open("data_2.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())   


def vertaa(luvut, pos):   #kutsutaan riveillä  96, 117
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


def vertaa2(luvut, pos):   # !!!!!!! korjaa kutsuu    
    print("  vertaa2")
    global safe_or_uns, safe
    ongelmat = []
    for i in range(len(luvut) -1):
        
        if pos:
            if int(luvut[i]) - int(luvut[i+1]) not in [1,2,3]:
                ongelmat.append(i)
        else:
            
            if int(luvut[i]) - int(luvut[i+1]) not in [-1,-2,-3]:
                ongelmat.append(i)

    if len(ongelmat) >= 1:   
        temp_luvut = copy.deepcopy(luvut)
        print("ongelmat", ongelmat, luvut)
        if len(luvut) - ongelmat[0] == 2: # toka vika ainoa ongelma, eli poistamalla vika ok !!
            safe += 1
        else:
            if len(ongelmat) >= 1:
                #fix(ongelmat[0], luvut, pos)
                luvut.pop(ongelmat[0])
                safe_or_uns.append(luvut)
                print("luvut", luvut)
            if len(ongelmat) >= 2:
                #fix(ongelmat[0], luvut, pos)
                temp_luvut.pop(ongelmat[1])
                safe_or_uns.append(temp_luvut)
                print("temp_luvut", temp_luvut)
       
    """
    elif ongelmat[0] == 1: # joudutaan tehdä uusi verrokki
        print("vertaa2 !!!", luvut)
        print(luvut)
        luvut.pop(ongelmat[0])
        print(luvut)
        safe_or_uns.append(luvut) """



def fix(ind, luvut, pos):
    global safe
    if pos:
        print("  FIX", int(luvut[ind-1]) - int(luvut[ind+1])) 

        if int(luvut[ind-1]) - int(luvut[ind+1]) not in [1,2,3]:
            print(int(luvut[ind-1]) - int(luvut[ind+1]))
            print("   fail")
        else:
            safe += 1
    else:
        if int(luvut[ind -1]) - int(luvut[ind+1]) not in [-1,-2,-3]:
            print(int(luvut[ind-1]) - int(luvut[ind+1]))
            print("   fail")
        else:
            safe += 1



def lue():
    global safe, unsafe
    
    for rivi in data:
        ok = 0
        luvut = rivi.split(" ")
        verrokki = int(int(luvut[0]) - int(luvut[1]))
        if verrokki in [1,2,3]:
            pos = True
            ok += vertaa(luvut, pos)
            safe += ok
        elif verrokki in [-1,-2,-3]:
            pos = False  
            ok += vertaa(luvut, pos)   
            safe += ok

        if ok == 0:
            """  wtf
            print("  luvut[1:]", luvut[1:])
            safe_or_uns.append(luvut[1:])
            luvut.pop(1)
            safe_or_uns.append(luvut)  """
            safe_or_uns.append(luvut)


def lue_array(a):  # pääohjelma kutsuu, poistettu yksi alkio
    global safe

    for rivi in a:
        verrokki = int(rivi[0]) - int(rivi[1])
        if verrokki in [1,2,3]:
            pos = True
            safe += vertaa(rivi, pos)
        elif verrokki in [-1,-2,-3]:
            pos = False  
            safe += vertaa(rivi, pos)   


def korjaa(unsafe):   # pääohj kutsuu lue() jälk
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
print("safe_or_uns", safe_or_uns)
lue_array(safe_or_uns)
print("safe jälkeen korjaa", safe)     #548, 558, 560 too low   , 568, 570, 572, 575, 593 not right
