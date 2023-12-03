data = []
cycle = 3   # ei mitään hajua miksei 0 tai 1 ole alkuarvo
x = 1
signal_strengths = []
xt = []

def readfile():   # a-kohta
    f = open("data.txt", "r")         
    for rivi in f:
            data.append(rivi.strip().split(" "))

def lue():
    global x, cycle, signal_strength
    cycles_of_interest = [20, 60, 100, 140, 180, 220]
    for rivi in data:        
        if 'noop' in rivi:            
            if cycle in cycles_of_interest:
                signal_strengths.append(cycle * x)
                xt.append(x)
            cycle += 1
        else:
            x += int(rivi[1])            
            if cycle in cycles_of_interest:
                signal_strengths.append(cycle * x)
                xt.append(x)
            cycle += 1
            if cycle in cycles_of_interest:
                signal_strengths.append(cycle * x)
                xt.append(x)
            cycle += 1

readfile()
lue()
print(signal_strengths)
print(xt)
print(sum(signal_strengths))
