
data = []
freq = 0


def readfile():
    f = open("data_easy2.txt", "r") 
    for rivi in f:
        luku = rivi.replace("+", "")
        data.append(int(luku.strip()))


def laske():
    global freq

    for luku in data:
            freq += luku
   
    return freq



readfile()
print(laske())
