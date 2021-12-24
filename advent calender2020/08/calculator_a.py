data = []
accumulator = 0
rows_visited = []


def readfile():   # a-kohta
    global output_values
    f = open("data.txt", "r") # a-kohta !!!!      
    for rivi in f:
        splitted = rivi.split(" ")
        if "+" in splitted[1]:
           splitted[1] =  splitted[1][1:]
        splitted[1] = int(splitted[1].strip())
        data.append(splitted)
    print(data)

def lue_ohjeet(rivi_nro):
    global accumulator
    if rivi_nro in rows_visited:
        return 
    else:
        rows_visited.append(rivi_nro)
    
    ohje, maara = data[rivi_nro]
    if ohje == "nop":
        lue_ohjeet(rivi_nro + 1)
    elif ohje == "acc":
        accumulator += maara
        lue_ohjeet(rivi_nro + 1)
    elif ohje == "jmp":
        lue_ohjeet(rivi_nro + maara)
    
    
readfile()
lue_ohjeet(0)
print(accumulator)
print(rows_visited)