data = []
sequence = "2333133121414131402"  # 2333133121414131402   file-free-file-free
sequence = "12345"
seq = []

def readfile():   
    global sequence
    f = open("data.txt", "r")         
    for rivi in f:
        sequence = rivi.strip()    


def muodostaSeq():
    global seq
    id = 0
    for i in range(len(sequence)):
        if i % 2 == 0:
            for times in range(int(sequence[i])):
                seq.append(id)
            id += 1
        else:
            for times in range(int(sequence[i])):
                seq.append(-1)

    print(seq)


def move_file_blocks():
    global seq
    seq_listana = list(seq)
    times = seq_listana.count(-1) 
    nro = -1
    for i in range(times):
        siirra = seq_listana[nro]
        if siirra != ".":
            ind = seq_listana.index(-1)
            seq_listana[ind] = siirra
            seq_listana[nro] = -1
        nro += -1

    l = seq_listana[seq_listana.index(-1):]
    epapisteet = [nro for nro in l if nro != -1]
    print(epapisteet)
    return (seq_listana[:seq_listana.index(-1)])


def checksum(l):
    print(l)
    sum = 0
    ind = 0
    for nro in l:
        sum += ind* int(nro)
        ind += 1

    print(sum)
        


readfile()
muodostaSeq()
checksum(move_file_blocks())   # 91649267962   too low   
                               # 6435922584968


