data = []
possible = 0

def readfile():   # a-kohta
    f = open("data.txt", "r")         
    for rivi in f:
        
        sp = rivi.strip().split("  ")
        if '' in sp:
            sp.remove('')
        for item in sp:
            data.append(int(item.strip()))
        

def lue():
    global possible
    offset = 0
    for i in range(int(len(data) / 9)):
        for i in range(3):                  # 3 peräkkäistä aloituskohtaa, sitten hyppy 9 yli suht. ekaan
            l1 = data[i + offset] 
            l2 = data[i + offset +3]
            l3 = data[i + offset +6]
            ehto1 = l1 + l2 > l3
            ehto2 = l1 + l3 > l2
            ehto3 = l2 + l3 > l1
            if (ehto1  and ehto2 and ehto3) :
                possible += 1
            print(l1, l2, l3)
        offset += 9


readfile()
print(data)
lue()
print(possible)  