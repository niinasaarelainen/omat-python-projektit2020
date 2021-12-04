
data = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(int(rivi.strip()))

def sums_of_three():
    edellinen = data[0]
    isompi_summa_lkm = 0
    for rivi_ind in range(len(data) - 3):
        summa = data[rivi_ind] + data[rivi_ind + 1] + data[rivi_ind + 2] 
        if summa > edellinen:
            isompi_summa_lkm += 1
        edellinen = summa
    return isompi_summa_lkm



readfile()
print(sums_of_three())