import copy

data = [0, 1, 2, 3, 4]
pos = 0
skip_size = 0
lengths = [3, 4, 1, 5]


def readfile():
    f = open("data_easy.txt", "r") 
    for rivi in f:
        data = rivi.strip().split(",")


def progress():
    global data, pos, skip_size
    for l in lengths:        
        data = list(reversed(data[pos:l])) + data[l:]
        pos += l + skip_size % len(data)
        skip_size += 1
        print(skip_size, data)




#readfile()
progress()
