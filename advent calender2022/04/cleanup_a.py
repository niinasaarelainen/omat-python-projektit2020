data = []

def readfile():
    f = open("data_1.txt", "r") 
    for rivi in f:
        data.append(rivi.strip().split(","))  # 2-4,6-8


def compare():  # 604 too high
    counter = 0
    for rivi in data:
        eka_start, eka_end = rivi[0].split("-")
        toka_start, toka_end = rivi[1].split("-")

        eka_start, eka_end = int(eka_start), int(eka_end) 
        toka_start, toka_end = int(toka_start), int(toka_end) 
        
        #case1:
        #.2345678. 
        #..34567..  
        if eka_start <= toka_start and eka_end >= toka_end:  # 21 99 3 22
            counter += 1

        #case2:
        #.....6...  
        #...456...
        elif toka_start <= eka_start and toka_end >= eka_end:
            counter += 1

    return counter

readfile()
print(compare())
