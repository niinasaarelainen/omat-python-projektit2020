
data = []


def readfile():   # a-kohta
    global crabs
    f = open("data_1rivi.txt", "r")         
    for rivi in f:
        luvut = []
        sp = rivi.strip().split(" ")
        for merkki in sp[1]:
            if merkki != ",":
                luvut.append(int(merkki))
        data.append([sp[0], luvut])
    print(data)

def montako_hashia():
    seqs_total = []
    seqs_rivi = []
    kyssarit_rivi = []
    for str, luvut in data:
        seq = 0
        kyssarit = 0
        for merkki in str:            
            if merkki == "#":
                seq += 1
            elif merkki == "?":
                kyssarit += 1
            else:
                if seq > 0:
                    seqs_rivi.append(seq)
                if kyssarit > 0:
                    kyssarit_rivi.append(kyssarit)
                seq = 0
                kyssarit = 0

        if seq > 0:
            seqs_rivi.append(seq)
        if kyssarit > 0:
            kyssarit_rivi.append(kyssarit)

        seqs_total.append(seqs_rivi)
        for s in seqs_rivi:
            luvut.remove(s)
        kyssarit_selvita(kyssarit_rivi, luvut)
        seqs_rivi = []
        kyssarit_rivi = []
    #print(seqs_total)

def kyssarit_selvita(kyssarit_rivi, luvut):
    success = 0
    hash_ind = 0
    for jono_x in kyssarit_rivi:
        luvut[hash_ind]



readfile()
montako_hashia()