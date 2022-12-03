
data = []
regs = {}

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip().split("if "))


def muodostaDic():
    for rivi in data:
        reg, op, am = rivi[0].strip().split(" ")
        if reg not in regs:
            regs[reg] = 0


def ehdot():
    for rivi in data:
        reg_ehto = rivi[1].split(" ")[0]
        str = "regs[\"" + reg_ehto + "\"]"
        ehto = str + " " + rivi[1].split(" ")[1] + " " + rivi[1].split(" ")[2]
        print(ehto)
        
        if eval(ehto):
            action = rivi[0].strip().replace("inc", "+").replace("dec", "-")
            reg, op, am = action.split(" ")   
            print("  reg", reg, "regs[reg]",  regs[reg])    
            regs[reg] = eval("regs[reg]" + op + am) 


readfile()
print(data)
muodostaDic()
ehdot()
print(regs)
print(max(regs.values()))
