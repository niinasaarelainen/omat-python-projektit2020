
data = []
regs = {}

def readfile():
    f = open("data_1.txt", "r") 
    for rivi in f:
        sp = rivi.strip().split(" ")
        data.append(sp)

def lue():
    #f = open("output.txt", "w") 
    i = 0
    while i < len(data):
        rivi = (data[i])
        print(rivi)
        if "cpy" in rivi:
            x = rivi[1]
            if x.isdigit():
                regs[rivi[2]] = int(x)
            else:
                regs[rivi[2]] = regs[x] 

        elif "inc" in rivi:
            regs[rivi[1]] += 1

        elif "dec" in rivi:
            regs[rivi[1]] -= 1

        elif "jnz" in rivi:
            x = rivi[1]
            if x.isdigit():
                i += int(rivi[2])
            elif x not in regs or regs[x] != 0: 
                i += int(rivi[2])
            else:
                i += 1
            continue   # ei tee i+=1

        """
        if 'b' in regs:
            print( "  b:", regs['b'])
        
        i += 1
        f.write(str(i)+", ")   # +1 vastaa .txt:n rivinumeroita suoraan """


print("moi")
readfile()
lue()
print("regs", regs)