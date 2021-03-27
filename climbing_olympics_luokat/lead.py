import operator, random


def pisteet_karsinta():      # 10 kilpailijaa, 8 finaaliin 
    pisteet = []
    top = 46.0
    pisteet.append(["Janja", top, 4.40])   # 3. parametri = aika, max 6 min
    pisteet.append(["Jain", 44.0, 5.0])    # Jain ja Julia kaikki samat    
    pisteet.append(["Julia", 44.0, 5.0])
    pisteet.append(["Jessica", 39.5, 5.50])
    pisteet.append(["Alex", 9.0, 2.41])
    pisteet.append(["AlexPlus", 9.5, 3.30])   # +
    pisteet.append(["AlexHidas", 9.0, 3.51])   # -
    pisteet.append(["Ihmelapsi", top, 4.41])
    pisteet.append(["Margo", 45.5, 5.11])
    pisteet.append(["Anna", 22.0, 4.41])

    s = sorted(pisteet, key=lambda s: (-s[1], s[2]) )  
    return s


def pisteet_finaali(sijoitukset):
    pisteet = []
    top = 48.0
    for i in range(8):
        if sijoitukset[i][0] == 'Janja':
            tulos =  random.randint(top/1.2*100, top*100)/100     # Janja pääsee väh. 5/6 reittiä
        else:
            tulos =  random.randint(top/2*100, top*100)/100
        aika = random.randint(200, 600)/100
        pisteet.append([sijoitukset[i][0], tulos, aika])   # 3. parametri = aika, max 6 min
        
    s = sorted(pisteet, key=lambda s: (-s[1], s[2]) )  
    return s


def tulokset(tulokset_list):
    tulokset = []
    sijoitus = 0
    tulokset.append([tulokset_list[0][0], sijoitus])    # eka on joka tapauksessa eka
    for i in range(1, len(tulokset_list)):
        # jos sama tulos ja sama aika
        if tulokset_list[i][1] == tulokset_list[i-1][1] and tulokset_list[i][2] == tulokset_list[i-1][2] :   
            tulokset.append([tulokset_list[i][0], sijoitus])
        else:            
            sijoitus = i        
            tulokset.append([tulokset_list[i][0], sijoitus])        
    
    return tulokset
        


pisteet_list = pisteet_karsinta()
karsintatulos = tulokset(pisteet_list)
print("\nL E A D -- KARSINTA")
for tulos in pisteet_list:
    pr = f"{tulos[0]}: {tulos[1]} (time:{tulos[2]:.2f})"   # 2 desimaalia
    print(pr) 
