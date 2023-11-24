data = []
total_string_code = 0  # isompi
total_memory = 0 #pienempi

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def kasittele():
    global total_string_code, total_memory
    for rivi in data:
        print(rivi)
        ind = 1   # ekaa " ei lasketa
        merkkeja_talla_rivilla = 0
        while ind < len(rivi)-1:
            if rivi[ind] == "\\" :
                print("\\")
                if rivi[ind + 1] == "x" :
                    print("x")
                    ind += 2
                elif rivi[ind + 1] == "\\" :
                    merkkeja_talla_rivilla += 1
                    ind += 1
                elif rivi[ind + 1] == "\"" :
                    print("\"")                
            else:
                merkkeja_talla_rivilla += 1

            ind += 1
        total_memory += merkkeja_talla_rivilla
        print("merkkeja_talla_rivilla", merkkeja_talla_rivilla)
        total_string_code += len(rivi)
                


readfile()
print(data)
kasittele()
print(total_string_code - total_memory)  #1468  too high, 1349  too low