
data = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        r = rivi.strip().split("\t")
        data.append(rivi.strip().split("\t"))


def checksum():
    sum = 0
    for rivi in data:
        #print("rivi", rivi)
        luvut = []
        for char in rivi:
            luvut.append(int(char))
        for l1 in luvut:
            for l2 in luvut:
                if l1 % l2 == 0 and l1 != l2:
                    sum += l1 / l2

    return int(sum)


readfile()
print(checksum())
 
