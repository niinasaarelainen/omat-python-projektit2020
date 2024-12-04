import copy

data = []
unsafe = []   # olisiko pärjännyt ilman tätä, safe laskettaisiin heti ?!?!
safe = 0
safe_or_uns = []

def readfile():
    f = open("data.txt", "r")  # data2 = 4,    data_oma1 = 4  data_oma2 = 3
    for rivi in f:
        data.append(rivi.strip())   


def vertaa(luvut, pos, listaanko):   
    global unsafe
    for i in range(len(luvut) -1):
        if pos:
            if int(luvut[i]) - int(luvut[i+1]) not in [1,2,3]:
                if listaanko:
                    unsafe.append(luvut)
                return 0       
        else:
            if int(luvut[i]) - int(luvut[i+1]) not in [-1,-2,-3]:
                print(int(luvut[i]) - int(luvut[i+1]))
                if listaanko:
                    unsafe.append(luvut)
                return 0
    print("  return 1§", luvut)
    return 1         


def vertaa2(luvut, pos):   # !!!!!!! korjaa kutsuu    
    global safe_or_uns, safe
    ongelma_ind = -1
    for i in range(len(luvut) -1):
        
        if pos:
            if int(luvut[i]) - int(luvut[i+1]) not in [1,2,3]:
                ongelma_ind = i
                break
        else:            
            if int(luvut[i]) - int(luvut[i+1]) not in [-1,-2,-3]:
                ongelma_ind = i
                break

    if ongelma_ind >= 0:   
        ok = 0
        temp_luvut2 = copy.deepcopy(luvut)
        temp_luvut3 = copy.deepcopy(luvut)
        print("ongelmat", ongelma_ind, luvut)
        luvut.pop(ongelma_ind)
        ok += lue_array_tentative(luvut) 
        temp_luvut3.pop(ongelma_ind+ 1)
        ok += lue_array_tentative(temp_luvut3) 
        if ongelma_ind > 0:
            temp_luvut2.pop(ongelma_ind- 1)
            ok += lue_array_tentative(temp_luvut2) 

        if ok > 0:        
            safe += 1



def lue_array_tentative(luvut):  # ongelmakohta kutsuu
    print(" lue_array_tentative", luvut)
    verrokki = int(luvut[0]) - int(luvut[1])
    if verrokki >= 0:
        pos = True
        return vertaa(luvut, pos, False)
    elif verrokki < 0:
        pos = False  
        return vertaa(luvut, pos, False)       

def lue():
    global safe, unsafe
    
    for rivi in data:
        ok = 0
        luvut = rivi.split(" ")
        verrokki = int(int(luvut[0]) - int(luvut[1]))
        if verrokki >= 0:
            pos = True
            ok += vertaa(luvut, pos, True)  # menee unsafe:iin
            safe += ok
        elif verrokki < 0:
            pos = False  
            ok += vertaa(luvut, pos, True)    # menee unsafe:iin
            safe += ok


def lue_array(a):  # pääohjelma kutsuu, poistettu yksi alkio
    global safe

    for rivi in a:
        verrokki = int(rivi[0]) - int(rivi[1])
        if verrokki >= 0:
            pos = True
            safe += vertaa(rivi, pos, False)
        elif verrokki < 0:
            pos = False  
            safe += vertaa(rivi, pos, False)   


def korjaa(unsafe):   # pääohj kutsuu lue() jälk
    global safe
    for rivi in unsafe:
        verrokki = int(int(rivi[0]) - int(rivi[1]))
        #print("verrooki", verrokki)
        if verrokki >= 0:
            pos = True
            vertaa2(rivi, pos)
        elif verrokki < 0:
            pos = False  
            vertaa2(rivi, pos)  
    
readfile() 
lue()
print("    unsafe", unsafe)
print("safe ennen korjaa-unsafe", safe)    
korjaa(unsafe)
#print("safe ennen korjaa-safe_or_uns", safe)    
print("safe_or_uns", safe_or_uns)
lue_array(safe_or_uns)
print("safe jälkeen korjaa", safe)     #548, 558, 560 too low   , 568, 570, 572, 575, 593, 562, 573, 578, 576, 584, 580, 577 not right
#577  !!