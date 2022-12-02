
data = []



def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def laske():
    sum = 0
    

    for rivi in data:
        edellinen = rivi[-1]
        for luku in rivi:
            if luku == edellinen:
                sum += int(luku)
            edellinen = luku
    
    return sum



readfile()
print(laske())
