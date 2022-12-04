import copy

#data = [0, 1, 2, 3, 4]
data = []

pos = 0
skip_size = 0
#lengths = [3, 4, 1, 5]
lengths = []

def create_data():
    for i in range(256):
        data.append(i)

def readfile():
    global lengths
    f = open("data.txt", "r") 
    for rivi in f:
        lengths = rivi.strip().split(",")


def progress():
    global data, pos, skip_size
    for len in lengths:  
        len = int(len)
        print(" len", len, "skip_size", skip_size,  "data", data)
        kaannettava_lista = []
        for i in range(len):
            kaannettava_lista.append(data[(pos + i) % data_len])
        
        kaannettava_lista =  list(reversed(kaannettava_lista))
        print(kaannettava_lista)

        for i in range(len):
            data[(pos + i) % data_len] = kaannettava_lista[i]
        pos += len + skip_size
        skip_size += 1
    
    print(" len", len, "skip_size", skip_size,  "data", data)


readfile()
create_data()
print(data)
data_len = len(data)
progress()
print(data[0] * data[1])
