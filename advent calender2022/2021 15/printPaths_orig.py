
m = []
loppuu_keskelle = []

def readfile():  
    f = open("data.txt", "r")         
    for rivi in f:
        rivi = rivi.strip()
        r = []
        for luku in rivi:
            r.append(int(luku))
        m.append(r)


def print_paths(row=0, col=0, s=""):
    
    #this is the recursive base case, if we're at the bottom right corner after this traversal, 
    #we're done with this path.
    if(row == (len(m) - 1) and col == (len(m[0]) - 1)): #I hard coded the index pair into the function, but this can be changed

        s += "->" + str(m[row][col]) #concatenate the final node onto the running total
        #print(s)
        return
        
    #If we overshot, no big deal, just don't count it among the solutions and return without printing.
    if(row > (len(m) - 1) or col > (len(m[0]) - 1)):
        return
        
    #recursively search each node below and to the right, and concatenate the current node to the running total.
    print_paths(row, col+1, s + "->" + str(m[row][col]))
    print_paths(row+1, col, s + "->" + str(m[row][col]))


def print_paths_oma(row=0, col=0, s=""):    
    
    #this is the recursive base case, if we're at the bottom right corner after this traversal, 
    #we're done with this path.        
        
    #If we overshot, no big deal, just don't count it among the solutions and return without printing.
    if(row > (len(m) - 1) or row < 0 or  col > (len(m[0]) - 1) or col < 0):
        return
    elif (m[row][col] == 8):
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
print_paths_oma()  
print(len(loppuu_keskelle))
for s in loppuu_keskelle:
    print(s)
print()
