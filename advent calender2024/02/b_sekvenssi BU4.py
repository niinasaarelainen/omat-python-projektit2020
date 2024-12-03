import copy

data = []
unsafe = []
unsafe2 = []
safe = 0
safe_or_uns = []

def readfile():
    f = open("data_2.txt", "r")  # data2 = 4,    data_oma1 = 4  data_oma2 = 3
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
        temp_luvut2 = copy.deepcopy(luvut)
        temp_luvut3 = copy.deepcopy(luvut)
        print("ongelmat", ongelmat, luvut)
        if len(luvut) - ongelmat[0] == 2: # toka vika ainoa ongelma, eli poistamalla vika ok !!
            safe += 1
        else:
            if len(ongelmat) >= 1:
                luvut.pop(ongelmat[0])
                safe_or_uns.append(luvut)
                if ongelmat[0] > 0:
                    temp_luvut2.pop(ongelmat[0]- 1)
                    if temp_luvut2 not in safe_or_uns :
                        safe_or_uns.append(temp_luvut2)   
                temp_luvut3.pop(ongelmat[0]+ 1)
                if temp_luvut3 not in safe_or_uns:
                    safe_or_uns.append(temp_luvut3)  
            """        
            if len(ongelmat) >= 2:
                temp_luvut.pop(ongelmat[1])
                if temp_luvut not in safe_or_uns:
                    safe_or_uns.append(temp_luvut)       """ 
    

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

        #if ok == 0:
        #    unsafe.append(luvut)


def lue_array(a):  # pääohjelma kutsuu, poistettu yksi alkio
    global safe

    for rivi in a:
        #print("lue_array", rivi)
        verrokki = int(rivi[0]) - int(rivi[1])
        if verrokki >= 0:
            pos = True
            safe += vertaa(rivi, pos, False)
        elif verrokki < 0:
            pos = False  
            safe += vertaa(rivi, pos, False)   

def lue_array_tentative(luvut):  # ongelmakohta kutsuu

    for rivi in a:
        #print("lue_array", rivi)
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
        """    
        else:
            rivi = rivi[1:]  
            verrokki = int(int(rivi[0]) - int(rivi[1]))
            print("verrooki", verrokki)
            if verrokki in [1,2,3]:
                pos = True
                vertaa2(rivi, pos)
            elif verrokki in [-1,-2,-3]:
                pos = False  
                vertaa2(rivi, pos)   """
    
readfile() 
lue()
print("    unsafe", unsafe)
print("safe ennen korjaa-unsafe", safe)    
korjaa(unsafe)
#print("safe ennen korjaa-safe_or_uns", safe)    
print("safe_or_uns", safe_or_uns)
lue_array(safe_or_uns)
print("safe jälkeen korjaa", safe)     #548, 558, 560 too low   , 568, 570, 572, 575, 593, 562, 573, 578, 576, 584, 580 not right
