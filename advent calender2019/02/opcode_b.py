import copy

data = []
data_copy = []

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        sp = rivi.split(",")
        for nro in sp:
            data.append(int(nro.strip()))


def x():
    for i in range(0,len(data_copy), 4):   # 4 välein
        if data_copy[i] == 1:
            data_copy[data_copy[i + 3]] = data_copy[data_copy[i +1]] + data_copy[data_copy[i + 2]]
        elif data_copy[i] == 2:
            data_copy[data_copy[i + 3]] = data_copy[data_copy[i +1]] * data_copy[data_copy[i + 2]]
        elif data_copy[i] == 99:
            break

def etsi_pari():
    global data_copy, data

    for eka in range(100):
        for toka in range(100):
            data_copy = copy.deepcopy(data)
            data_copy[1] = eka
            data_copy[2] = toka
            x()
            if data_copy[0] == 19690720:
                return (eka, toka)


readfile()
noun , verb = etsi_pari()
#print(data)
print(100 * noun + verb)
