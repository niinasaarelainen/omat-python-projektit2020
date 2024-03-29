
ind = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

m = [[1, 1, 3],
     [1, 2, 6],
     [1, 1, 1]]


vastaukset = []

def print_paths(row=0, col=0, s=""):
    
    #this is the recursive base case, if we're at the bottom right corner after this traversal, 
    #we're done with this path.
    if(row == (len(m) - 1) and col == (len(m[0]) - 1)): #I hard coded the index pair into the function, but this can be changed

        s += str(m[row][col]) #concatenate the final node onto the running total
        if s not in vastaukset:
            vastaukset.append(s)
        return
        
    #If we overshot, no big deal, just don't count it among the solutions and return without printing.
    if(row > (len(m) - 1) or col > (len(m[0]) - 1)):
        return
        
    #recursively search each node below and to the right, and concatenate the current node to the running total.
    print_paths(row, col+1, s + str(m[row][col]))
    print_paths(row+1, col, s + str(m[row][col]))



def print_paths_mutkittelee(row=0, col=0, s="", ind_str=""):
    
    #this is the recursive base case, if we're at the bottom right corner after this traversal, 
    #we're done with this path.
    if(row == (len(m) - 1) and col == (len(m[0]) - 1)): #I hard coded the index pair into the function, but this can be changed

        s += str(m[row][col]) #concatenate the final node onto the running total
        vastaukset.append(s)
        return
        
    #If we overshot, no big deal, just don't count it among the solutions and return without printing.
    if(row > (len(m) - 1) or col > (len(m[0]) - 1)):
        return    
        
    #recursively search each node below and to the right, and concatenate the current node to the running total.
    
    if str(ind[row][col-1]) not in ind_str and col-1 >= 0:
        print_paths_mutkittelee(row, col-1, s + str(m[row][col]), ind_str + str(ind[row][col]))
    else:
        print_paths_mutkittelee(row+1, col, s + str(m[row][col]), ind_str + str(ind[row][col]))

    if str(ind[row-1][col]) not in ind_str and row-1 >= 0:
        print_paths_mutkittelee(row-1, col, s + str(m[row][col]), ind_str + str(ind[row][col]))  
    else:
        print_paths_mutkittelee(row, col+1, s + str(m[row][col]), ind_str + str(ind[row][col]))


print_paths_mutkittelee()  # oletusarvoilla
print_paths()

sums = []
for v in vastaukset:
    sum = 0
    for nro in v:
        sum += int(nro)
    sums.append(sum)

print(min(sums))


"""if str(m[row][col-1]) not in s and col-1 >= 0:
        print_paths(row, col-1, s + str(m[row][col]))
    else:
        print_paths(row+1, col, s + str(m[row][col]))
    print_paths(row, col+1, s + str(m[row][col]))    
"""