data = []


def readfile():   # a-kohta
    global data
    f = open("data.txt", "r")         
    for rivi in f:
        numerot_str = rivi.split(",")
        for nro in numerot_str:
            data.append(int(nro))
    print(data)




readfile()
()
