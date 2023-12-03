data = []

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip().split(","))  # 2-4,6-8


def overlap():  
    counter = 0
    for rivi in data:
        eka_start, eka_end = rivi[0].split("-")
        toka_start, toka_end = rivi[1].split("-")

        eka_start, eka_end = int(eka_start), int(eka_end) 
        toka_start, toka_end = int(toka_start), int(toka_end) 
        
        #case1:
        # 4-8, 2-6
        if eka_start <= toka_end and eka_end >= toka_start:
            counter += 1
            #print(eka_start, eka_end, toka_start, toka_end)

        #case2:
        # 2-6,4-8
        elif toka_start <= eka_end and toka_end >= eka_start: 
            counter += 1

    return counter

readfile()
print(overlap())
