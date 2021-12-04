data = []



def readfile():
    x = 0
    y = 0
    f = open("data.txt", "r") 
    for rivi in f:
        luku = rivi.split()[1]
        if "forward" in rivi:            
            x += int(luku.strip())
        if  "down" in rivi:
            y += int(luku.strip())
        if "up" in rivi:
            y -= int(luku.strip())
    return(x, y)


readfile()
x, y = readfile()
print(x * y)