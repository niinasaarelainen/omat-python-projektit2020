data = []
m = []
loppuu_keskelle = []
end = ord("E")

def readfile():  
    f = open("data_1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())


def muunnaNumeroiksi():
    for rivi in data:
        r = []
        for kirjain in rivi:
            r.append(ord(kirjain))
        m.append(r)
        r = []



def print_paths_oma(row=0, col=0, s=""):    
    
    #this is the recursive base case, if we're at the bottom right corner after this traversal, 
    #we're done with this path.        
        
    #If we overshot, no big deal, just don't count it among the solutions and return without printing.
    if(row > (len(m) - 1) or row < 0 or  col > (len(m[0]) - 1) or col < 0):
        return
    elif (m[row][col] == end):
            s += "," + str(m[row][col]) #concatenate the final node onto the running total
            loppuu_keskelle.append(s)
            return
    
        
    #recursively search each node below and to the right, and concatenate the current node to the running total.
    if str(m[row][col]) not in s:
        #if (m[row][col+1] - m[row][col] in [0, 1] )
        print_paths_oma(row, col+1, s + "," + str(m[row][col]))
        print_paths_oma(row, col-1, s + "," + str(m[row][col]))
        print_paths_oma(row+1, col, s + "," + str(m[row][col]))
        print_paths_oma(row-1, col, s + "," + str(m[row][col]))
        


readfile()
muunnaNumeroiksi()
print(m)
print_paths_oma()  
print(len(loppuu_keskelle))
#loppuu_keskelle = loppuu_keskelle[2:5]
loppuu_keskelle.append(",83,77,78,79,80,81")

for s in loppuu_keskelle:
    sp = s.strip().split(",")[2:-1]
    
    merkki = 1
    ok = True
    while (int(sp[merkki]) - int(sp[merkki -1]) in [0, 1] and merkki < len(sp) -1):
        print(sp[merkki], sp[merkki-1])
        merkki += 1
    if merkki != len(sp)-1:
        ok = False
    if ok:
        print(sp)
        
print()
