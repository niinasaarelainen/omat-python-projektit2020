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
            s += "->" + str(m[row][col]) #concatenate the final node onto the running total
            loppuu_keskelle.append(s)
            return
    
        
    #recursively search each node below and to the right, and concatenate the current node to the running total.
    if str(m[row][col]) not in s:
        print_paths_oma(row, col+1, s + "->" + str(m[row][col]))
        print_paths_oma(row, col-1, s + "->" + str(m[row][col]))
        print_paths_oma(row+1, col, s + "->" + str(m[row][col]))
        print_paths_oma(row-1, col, s + "->" + str(m[row][col]))
        


readfile()
muunnaNumeroiksi()
print(m)
print_paths_oma()  
print(len(loppuu_keskelle))

for s in loppuu_keskelle:
    for merkki in range(len(s)-2):
        if (int(s[merkki]) - int(s[merkki +1]) != -1):    # TODO
            continue
        print(s)
print()
