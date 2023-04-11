
data = []


def readfile():
    global stringi
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(int(rivi.strip()))


def action():
    ind = 0
    steps = 0
    while ind < len(data):
        ind_new = data[ind]
        if data[ind] >= 3:
             data[ind] -= 1
        else:
            data[ind] += 1
        ind += ind_new
        steps += 1

    return steps


readfile()
print(data)
print(action())
 
 