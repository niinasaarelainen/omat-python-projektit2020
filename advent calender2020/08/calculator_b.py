import copy

data = []
data_kopio = []
accumulator = 0
accumulator_all = []
rows_visited = []
negatiiviset_jumpit = []


def readfile():   # a-kohta
    global output_values
    f = open("data.txt", "r") # a-kohta !!!!      
    for rivi in f:
        splitted = rivi.split(" ")
        if "+" in splitted[1]:
           splitted[1] =  splitted[1][1:]
        splitted[1] = int(splitted[1].strip())
        data.append(splitted)
        data_kopio.append(splitted)
    data.append(["END", 0])
    data_kopio.append(["END", 0])


def lue_ohjeet(data, rivi_nro):
    global accumulator

    #print("rivi_nro ", rivi_nro)
    if rivi_nro in rows_visited:
        print("    FAIL")
        return 0
    else:
        rows_visited.append(rivi_nro)

    ohje = data[rivi_nro][0]
    maara = data[rivi_nro][1]

    if ohje == "nop":
        return lue_ohjeet(data, rivi_nro + 1)
    elif ohje == "acc":
        accumulator += maara
        print(ohje, maara)
        return lue_ohjeet(data, rivi_nro + 1)
    elif ohje == "jmp":
        return lue_ohjeet(data, rivi_nro + maara)
    elif ohje == "END":
        print("    END")
        return "END"

    print("tänne meni", rivi_nro, ohje)
    #täältä palautuu None ja se ei käy


def etsi_negatiiviset_jumpit():
    global data_kopio, data, accumulator, rows_visited
    accumulator = 0

    #luetaan dataa, ja tehdään muutokset data_kopioon joka lähetetään --> lue_ohjeet
    for i in range(len(data)):
        ohje, maara = data[i]        
        if ohje == "jmp" and maara < 0:
            print("i: ", i)
            data_kopio[i][0] = "nop"
            print("data_kopio ", data_kopio)
            returni = lue_ohjeet(data_kopio, 0)
            print("returni", returni)
            rows_visited = []
            print("(accumulator)", accumulator)

            if returni == "END":
                accumulator_all.append(accumulator)
            
            accumulator = 0
        data_kopio = copy.deepcopy(data)
        
    
        


    
    
readfile()
etsi_negatiiviset_jumpit()
print(max(accumulator_all))
#lue_ohjeet(data, 0)

#print(rows_visited)