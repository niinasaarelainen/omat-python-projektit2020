
data = []
data2 = []


def readfile():
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())    # oxygen käyttää tätä
        data2.append(rivi.strip())   # co2 käyttää tätä


def laske_oxygen(g):
    global data    
    bin_pituus = len(g)
    print("len(data)", len(data))
    ekat_nrot = "" 
    oikea_rivi = ""
    vaara_rivi = "110111000111"
    for i in range(bin_pituus):   # bin_pituus
        oxygen = []
        for rivi in data:            
            ekat_nrot += rivi[i]
            if rivi[i] == g[i]:
                oxygen.append(rivi)
            
        data = oxygen  
        #print(ekat_nrot)
        print(len(oxygen))  
        if len(oxygen) == 1:
            return oxygen    
        g = maarat_ja_g(bin_pituus, data)


def maarat_ja_g(bin_pituus, data):
    maarat = []
    for i in range(bin_pituus):
        maarat.append(0)
    for rivi in data:
        for i in range(len(rivi)):
            maarat[i] += int(rivi[i])
    g = laske_gamma_o(maarat, data)
    return g


def laske_co2(g):
    global data2    
    bin_pituus = len(g)
    
    for i in range(bin_pituus):
        co2 = []
        for rivi in data2:
            if rivi[i] != g[i]:
                co2.append(rivi)
            
        data2 = co2     
        #print(data2)
        if len(data2) == 255:
            print(data2)
        print("len(co2)", len(co2))
        if len(co2) == 1:
            return co2
        g = maarat_ja_g(bin_pituus, data2)    

    
def laske_gamma_o(maarat, data):
    g = ""
    for lkm in maarat:
        if len(data) % 2 == 1:            
            if lkm > len(data)//2:
                g += "1"
            else:
                g += "0"
        if len(data) % 2 == 0:            
            if lkm >= len(data)//2:
                g += "1"
            else:
                g += "0"
    #print("g", g)
    return g
   

def decode():
    maarat = []
    for i in range(len(data[0])):
        maarat.append(0)
    for rivi in data:
        for i in range(len(rivi)):
            maarat[i] += int(rivi[i])
    gamma_rate_o = laske_gamma_o(maarat, data)
    ox = laske_oxygen(gamma_rate_o)
    co2 = laske_co2(gamma_rate_o)
    print( "ox, co2: " ,ox, co2)
    return ox, co2


def binary_to_decimal(b_num):
    b_num = list(b_num)
    value = 0
    for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
            value = value + pow(2, i)
    return value



readfile()
g, e = decode()
g = binary_to_decimal(g[0])
e = binary_to_decimal(e[0])
print("g, e:", g, e)
print(g * e)