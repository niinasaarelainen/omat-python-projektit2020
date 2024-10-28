data = []
n_numbers = []
#find = 127 
find = 1721308972    # vaihda !!!!!!!!!!!!


def readfile():  
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(int(rivi.strip()))
    print(data)
   

def validOrNot():
    global data, n_numbers
    for aloitusind in range(len(data)-1):
        summa = data[aloitusind]        
        seuraajaind = aloitusind + 1
        seuraaja = data[seuraajaind]
        nrot = [summa]
        while summa < find and seuraajaind < len(data):
            summa += seuraaja
            nrot.append(seuraaja)
            seuraajaind += 1
            seuraaja = data[seuraajaind]
            if summa == find:
                return nrot   # oikeasti list
                



readfile()
min = min(validOrNot())
max = max(validOrNot())
print(min + max)