
"""
def super_arrays(lista, new_list):
    if len(lista) == 2:
        new_list.append(lista)
        return 
   
    
    vika = lista.pop(-1)
    new_list.append(vika)
    new_list.append(super_arrays(lista, new_list))
    return  new_list """
    
def super_arrays(lista, new_list):
    if len(lista) == 0:
        return 0

    else:
        uusin=[]
        
        tail = lista[0]
        smaller_list = lista[1:]
        new_list.append(tail)
        uusin.append(new_list)
        print("uusin", uusin)
        super_arrays(smaller_list, uusin)
        return uusin


    """

def super_arrays(lista, new_list, uusin_lista):
    if len(lista) == 2:
        new_list.append(lista)
        return  
   
    
    new_list.append(lista.pop(-1))
    uusin_lista = []
    uusin_lista.append(new_list)
    super_arrays(lista, new_list, uusin_lista)
    return uusin_lista """

print(super_arrays([1,2,3], [])) 
print(super_arrays([1,2,3,4,5], [])) 