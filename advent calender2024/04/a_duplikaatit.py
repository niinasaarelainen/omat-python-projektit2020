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

    for super_y in range(len(data)):
        for aloitusrivi in range(len(data[0])):
            rivi = ""  
            for y in range(len(data)):   
                if y+aloitusrivi < len(data) and y+super_y < len(data):           
                    rivi += data[y+super_y][y+aloitusrivi]
            print(rivi)
            montako += rivi.count("XMAS")
            montako += rivi.count("SAMX")


def diagonal_ylos():  # /   liikaa duplikaatteja
    global montako
    
    for super_y in range(len(data)-1, -1, -1):
        for aloitusrivi in range(len(data)-1, -1, -1):
            rivi = ""  
            for y in range(len(data)):   
                if super_y-y < len(data) and y+aloitusrivi < len(data):           
                    rivi += data[super_y-y][y+aloitusrivi]
            print(rivi)
            montako += rivi.count("XMAS")
            montako += rivi.count("SAMX")



readfile()
#horizontal()
#vertical()
#diagonal_alas()
diagonal_ylos()
print(montako)