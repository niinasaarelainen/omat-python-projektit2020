def etsi_min_2_param(lista, pienin):
    
    if len(lista) == 0:
        return None    
    elif len(lista) == 1:
        return min(pienin, lista[0])
    else:    
        eka = lista.pop(0)
        if eka < pienin:
            pienin = eka
        
        return etsi_min_2_param(lista, pienin)


print("\npienin, 2 param:")
print(etsi_min_2_param([2], 1000))
print(etsi_min_2_param([3, 2], 1000))
print(etsi_min_2_param([4, 3, 2], 1000))
print(etsi_min_2_param([2, 4, 3], 1000))
print(etsi_min_2_param([2, 4, 1, 6, 8, 10], 1000))
print(etsi_min_2_param([], 1000))

#################################################################################

def etsi_max_2_param(lista, suurin):
    if lista == []:        
        return suurin   
    
    eka = lista.pop(0)
    if eka > suurin:
        suurin = eka
    
    return etsi_max_2_param(lista, suurin)

print("\nsuurin, 2 param:")
print(etsi_max_2_param([4, 3, 2], -1000))
print(etsi_max_2_param([2, 4, 1, 6, 8, 10], -1000))
print(etsi_max_2_param([], -1000))

#################################################################################

def etsi_min_1_param(lista):
    if len(lista) == 0:
        return None     
    if len(lista) == 1:        
        return lista[0]   
    
    pienin = lista[0]
    verrokki = lista[1]
    if verrokki < pienin:
        lista[0] = verrokki 
    lista.remove(verrokki)
    
    return etsi_min_1_param(lista)

print("\npienin, 1 param:")
print(etsi_min_1_param([]))
print(etsi_min_1_param([2]))
print(etsi_min_1_param([3, 2]))
print(etsi_min_1_param([4, 3, 2]))
print(etsi_min_1_param([1, 4, 11, 6, 8, 10]))    # pienin alussa
print(etsi_min_1_param([2, 4, 1, 6, 8, 10]))       # pienin keskellä
print(etsi_min_1_param([11, 4, 11, 6, 8, 10, 1]))    # pienin lopussa
