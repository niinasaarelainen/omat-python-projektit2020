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
        ind = 0   # ekaa " ei lasketa
        merkkeja_talla_rivilla = 0
        while ind < len(rivi):
            if rivi[ind] == "\"" :
                print("hipsu")
                merkkeja_talla_rivilla += 2
            elif rivi[ind] == "\\" :
                print("keno")
                merkkeja_talla_rivilla += 2
                   
            else:
                merkkeja_talla_rivilla += 1

            ind += 1
        
        merkkeja_talla_rivilla += 2
        print("merkkeja_talla_rivilla", merkkeja_talla_rivilla)
        total_memory += merkkeja_talla_rivilla
        total_string_code += len(rivi)
                


readfile()
print(data)
kasittele()
print( total_memory - total_string_code) 