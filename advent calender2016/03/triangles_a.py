data = []
possible = 0

def readfile():   # a-kohta
    f = open("data.txt", "r")         
    for rivi in f:
            data.append(rivi.strip().split("  "))

def lue():
    global possible
    for rivi in data:
        if '' in rivi:
            rivi.remove('')
        ehto1 = int(rivi[0].strip()) + int(rivi[1].strip()) > int(rivi[2].strip())
        ehto2 = int(rivi[0].strip()) + int(rivi[2].strip()) > int(rivi[1].strip())
        ehto3 = int(rivi[1].strip()) + int(rivi[2].strip()) > int(rivi[0].strip())
        if (ehto1  and ehto2 and ehto3) :
            possible += 1
            print(rivi)


readfile()
print(data)
lue()
print(possible)  # 1583 too high