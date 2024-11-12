data = []
hash = {0: [1, 2], 1: ["a"], 2: [[1, 3],[3, 1]], 3: ["b"]}
vastaukset = []


def readfile():   # a-kohta
    global data
    f = open("data.txt", "r")         
    for rivi in f:
        rivi = rivi.replace("(", " ( ")
        data.append(rivi.strip().split(" "))
    print(data)


def readHash(ind, vastaus):
    for item in hash[ind]:  
        print(ind)          
        if isinstance(item, list):
            for nro in item:
                print(nro, "**list")
                vastaus += readHash(nro, vastaus)
        elif isinstance(item, str):
            vastaus += item
            print(vastaus)
            if len(vastaus) == 4:
                vastaukset.append(vastaus)
                return ""
            else:
                return vastaus
        else:
            print(item, "**nro")
            vastaus += readHash(item, vastaus)


    print(vastaukset)



#readfile()
readHash(0, "")
