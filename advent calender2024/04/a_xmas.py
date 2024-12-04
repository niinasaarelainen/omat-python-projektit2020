data = []
montako = 0

def readfile():
    f = open("data_diag2.txt", "r")   # data_1 = 18
    for rivi in f:
        data.append(rivi.strip())


def horizontal():
    global montako
    for rivi in data:
        montako += rivi.count("XMAS")
        montako += rivi.count("SAMX")

def vertical():
    global montako
    for x in range(len(data[0])):
        rivi = ""
        for y in range(len(data)):
            rivi += data[y][x]
        print(rivi)
        montako += rivi.count("XMAS")
        montako += rivi.count("SAMX")

def diagonal_alas():  # \
    global montako
    pass


def diagonal_ylos():  # /   liikaa duplikaatteja
    global montako

    """
    # yläpuolisko: y muuttuu, x alkaa aina 0:sta 
    for y in range(len(data)):
        rivi = ""  
        aloitus_x = 0
        nykyinen_y = y
        for x in range(y +1):
            
            if 0 <= y < len(data) and 0 <= x < len(data):     
                rivi += data[nykyinen_y - x][x]
        if rivi != "":    
            print(rivi)
        montako += rivi.count("XMAS")
        montako += rivi.count("SAMX")   """


    # alapuolisko: y = alin rivi, x muuttuu
    for x in range(len(data)):
        rivi = ""  
        aloitus_x = 0
        nykyinen_x = x
        for y in range(x +1):
            
            if 0 <= y < len(data) and 0 <= x < len(data):     
                rivi += data[y - nykyinen_x][nykyinen_x]
        if rivi != "":    
            print(rivi)
        montako += rivi.count("XMAS")
        montako += rivi.count("SAMX")


    


readfile()
#horizontal()
#vertical()
#diagonal_alas()
diagonal_ylos()
print(montako)