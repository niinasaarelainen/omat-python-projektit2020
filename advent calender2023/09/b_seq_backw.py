data = []
sequence = []
sequences = []
matkat = []
sequence_ALL = []
vastaukset = 0


def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip().split(" "))    


def luo_seq():
    global sequence_ALL
    for rivi in data:
        sequence = []
        sequence_ALL = []
        for i in rivi:
            if i != "":
                sequence.append(int(i.strip()))
        valimatkat(sequence)
        sequence_ALL_kaylapi()
        #sequences.append(sequence)

    
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
        #print(matkat, "REKURSOI")
        valimatkat(matkat)
    else:
        pass
        #print(matkat, "YES")

def sequence_ALL_kaylapi():
    global vastaukset
    lisataan_seuraavaan = 0
    for seq in reversed(sequence_ALL):
        seq.insert(0, seq[0]- lisataan_seuraavaan)    # !! insert ja mihin, ei append
        lisataan_seuraavaan = seq[0]
        print("seq", seq)
        print("lisataan_seuraavaan", lisataan_seuraavaan)

    print(sequence_ALL[0][0] )
    vastaukset += sequence_ALL[0][0] 
        



readfile()
luo_seq()
"""
for seq in sequences:
    print(sequence)
    valimatkat(seq)
    #valimatkat([0])    TODO joku merkki seq välille
print(sequence_ALL) """


print("vastaus:", vastaukset )