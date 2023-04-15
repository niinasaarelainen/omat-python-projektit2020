import copy

muunna_krs = {4:0, 3:1, 2:2, 1:3}    # mika kerros : array-y
kerrokset = []
data = []

def readfile():
    global data
    f = open("data_1.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def read_data():  
    for rivi in data:
        print(rivi)
    kerrokset.append([])         # 4. krs tyhjä
    kerrokset.append(["LG"])      # 3.
    kerrokset.append(["HG"])       # 2.
    kerrokset.append(["E, HM, LM"]) # 1.
    

readfile()
read_data()
