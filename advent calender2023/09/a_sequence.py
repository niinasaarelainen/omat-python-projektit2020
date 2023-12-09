data = []
sequence = []
matkat = []


def readfile():   
    f = open("data_1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip().split("  "))


def luo_seq():
    for rivi in data:
        for i in rivi:
            if i != "":
                sequence.append(int(i.strip()))
    
def valimatkat(sequence):
    global matkat
    matkat = []
    uusinta = False
    for ind in range(len(sequence)-1):
        vali = sequence[ind+1] - sequence[ind]
        if vali != 0:
            uusinta = True
        matkat.append(vali)

    if uusinta:
        print(matkat, "REKURSOI")
        valimatkat(matkat)
    else:
        print(matkat, "YES")
        #break 


readfile()
luo_seq()
print(sequence)
valimatkat(sequence)