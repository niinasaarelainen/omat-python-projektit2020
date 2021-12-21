
import copy

timers = []
kaloja_0_8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def readfile():   # a-kohta
    global timers
    f = open("data.txt", "r")         
    for rivi in f:
        numerot_str = rivi.split(",")
        for nro in numerot_str:
            timers.append(int(nro))
        print(timers)

def readfile2():    # b-kohta
    global timers
    f = open("data.txt", "r")         
    for rivi in f:
        numerot_str = rivi.split(",")
        for nro in numerot_str:
            kaloja_0_8[int(nro)] += 1
        print(kaloja_0_8)

def tutki():
    for nro in range(len(timers)):
        if timers[nro] > 0:
            timers[nro] -= 1
        else:
            timers[nro] = 6
            timers.append(8)
    #print(timers)
                             # 18 days, there are a total of 26 fish    35
def tutki2():    # After 80 days, there would be a total of 5934.   5115
    
    days = 256
    for day in range(days):  
        temp = copy.deepcopy(kaloja_0_8)
        for ind in reversed(range(8)): 
            kaloja_0_8[ind] = temp[ind + 1]
            if ind == 0:
                kaloja_0_8[6] += temp[0]
                kaloja_0_8[8] = temp[0]
        print(kaloja_0_8)           
    

readfile2()
tutki2()
print(sum(kaloja_0_8))

