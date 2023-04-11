import copy

data = []
tulokset = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        r = rivi.split("\t")
        for luku in r:
            data.append(int(luku))    # voi olla "monta planeettaa"

    print(data)


def tutki():    
    steps = 0
    banks = len(data)
    
    while tulokset.count(data) < 2  :   
        m = max(data)
        ind = data.index(m)
        luku = data[ind]
        print("luku", luku)
        data[ind] = 0
        ind += 1
       
        if luku % banks == 0:
            for i in range(banks):
                data[ind % banks] += int(luku / banks)
                ind += 1
                #print(data)
        else:
            for l in range(luku % banks):
                data[ind% banks] += int(luku / banks) + 1
                ind += 1
                #print(data)
            for l in range(banks - luku % banks):
                data[ind% banks] += int(luku / banks) 
                ind += 1
                #print(data)

        tulos = copy.deepcopy(data)
        tulokset.append(tulos)
        steps += 1

   
    return steps
    


readfile()
print(tutki())