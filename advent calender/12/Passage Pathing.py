
paths = {"start": ["kj", "HN", "dc"], "kj": ["sa", "HN", "dc"], "HN": ["kj", "dc", "end"], "dc": ["LN", "end", "HN", "kj"], "sa": ["kj"], "LN": ["dc"]}
data = []

def readfile():   # a-kohta
    global crabs
    f = open("data.txt", "r")         
    for rivi in f:
        numerot_str = rivi.split(",")
        for nro in numerot_str:
            data.append(int(nro))
    print(data)


""" rekursiomalli:   """
def Recur_facto(n): 
    
    if (n == 0): 
        return 1

    print(n * Recur_facto(n-1) )
    return n * Recur_facto(n-1) 
    

def paths_find(node, matka):
    for target in paths[node]:
        if target == "end":
            return matka
        elif target not in matka:
            matka.append(target)
            print(matka)
        return paths_find(target, matka)


print("lopputulos", Recur_facto(3))
#print(Recur_facto(6))
#readfile()
matka = []
paths_find("start", matka)
