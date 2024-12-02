data = []
sequence = []
sequences = []
matkat = []
sequence_ALL = []
vastaukset = 0


def readfile():   
    f = open("data_1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip().split(" "))
    


def luo_seq():
    for rivi in data:
        sequence = []
        for i in rivi:
            if i != "":
                sequence.append(int(i.strip()))
        sequences.append(sequence)

    
def valimatkat(sequence):
    global matkat
    matkat = []
    uusinta = False
    sequence_ALL.append(sequence)

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

def sequence_ALL_kaylapi():
    global vastaukset
    lisataan_seuraavaan = 0
    for seq in reversed(sequence_ALL):
        seq.append(lisataan_seuraavaan + seq[-1])
        lisataan_seuraavaan = seq[-1]
        print("seq", seq)
        print("lisataan_seuraavaan", lisataan_seuraavaan)

    vastaukset += sequence_ALL[0][-1] 
        



readfile()
luo_seq()
for seq in sequences:
    print(sequence)
    valimatkat(seq)
print(sequence_ALL)

sequence_ALL_kaylapi()

print("vastaus:", vastaukset )