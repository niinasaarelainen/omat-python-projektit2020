
data = []
opcodes = [1, 2, 99]


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        sp = rivi.split(",")
        for nro in sp:
            data.append(int(nro.strip()))


def x():
    for i in range(0,len(data), 4):   # 4 välein
        if data[i] == 1:
            data[data[i + 3]] = data[data[i +1]] + data[data[i + 2]]
        elif data[i] == 2:
            data[data[i + 3]] = data[data[i +1]] * data[data[i + 2]]
        elif data[i] == 99:
            break




readfile()
print(data)
# replace position 1 with the value 12 and replace position 2 with the value 2
data[1] = 12
data[2] = 2
x()
print(data)
print()
