import math

data = []  # strings
flashes = 0
flash_cordinates = []


def readfile():   # a-kohta
    global data
    f = open("data_easy.txt", "r")         
    for rivi in f:
        data.append([])
        for nro in rivi.strip():
            data[-1].append(int(nro))
    print(data)


def flash(rivi_nro, monesko):
    global data, flashes
    # any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, 
    # including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, 
    # it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. 
    # (An octopus can only flash at most once per step.)
    for rivi in range(-1, 2):
        for x in range(-1, 2):
            rivi_nr = rivi_nro + rivi
            monesk = monesko + x
            #print("rivi_nro", rivi_nr, "monesko", monesk)
            if data[rivi_nr][monesk] != None:
                data[rivi_nr][monesk] += 1   
            if rivi_nr >= 0 and monesk  >= 0 and data[rivi_nr][monesk] == 10:
                flash_cordinates.append([rivi_nr,monesk] )                
                flashes += 1
                data[rivi_nr][monesk] = None   # None = olen jo flashahtanyt 

   
    print(data)


def nollaa():
    # Finally, any octopus that flashed during this step has its energy level set to 0

    for rivi_nro in range(len(data)):
        for monesko in range(len(data[rivi_nro])):  
            if data[rivi_nro][monesko] == None:
                data[rivi_nro][monesko] = 0    
    print("nollauksen jälk", data)  


def flash_proseduuri():
    global data
    # First, the energy level of each octopus increases by 1.
    for rivi_nro in range(len(data)):
        for monesko in range(len(data[rivi_nro])):                     
            if data[rivi_nro][monesko] == None:
                flash(rivi_nro, monesko)
            elif data[rivi_nro][monesko] >= 9: 
                flash(rivi_nro, monesko)
    nollaa()

    print(data)

    

   
readfile()
flash_proseduuri()
()


