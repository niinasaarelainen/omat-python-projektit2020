data = []


def readfile():
    global data
    f = open("data.txt", "r")   
    
    for rivi in f:
        data.append([])
        sanat = rivi.strip().split(" ")
        for sana in sanat:
            data[-1].append(sorted(sana))
        

    
def valids():
    valid = 0
    invalid = 0
    for rivi in data:
        validko = True
        for word in rivi:
            if rivi.count(word) > 1:
                invalid += 1
                validko = False
                break
        if validko:
            valid += 1
    
    return valid, invalid
        




readfile()
print(data)
print(valids())