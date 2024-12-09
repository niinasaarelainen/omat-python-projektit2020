data = []
sequence = "2333133121414131402"  # 2333133121414131402   file-free-file-free
#sequence = "12345"
seq = ""

def readfile():   
    global sequence
    f = open("data_1.txt", "r")         
    for rivi in f:
        sequence = rivi.strip()    


def muodostaSeq():
    global seq
    id = 0
    for i in range(len(sequence)):
        if i % 2 == 0:
            seq += str(id) * int(sequence[i])
            id += 1
        else:
            seq += "." * int(sequence[i])

    print(seq)


def move_file_blocks():
    global seq
    seq_listana = list(seq)
    times = seq_listana.count(".")
    nro = -1
    for i in range(times):
        siirra = seq_listana[nro]
        if siirra != ".":
            ind = seq_listana.index(".")
            seq_listana[ind] = siirra
            seq_listana[nro] = "."
        nro += -1

    return (seq_listana[:seq_listana.index(".")])


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
checksum(move_file_blocks())


