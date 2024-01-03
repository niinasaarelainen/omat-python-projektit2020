m = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

def print_paths(row=0, col=0, s=""):
    
    #this is the recursive base case, if we're at the bottom right corner after this traversal, 
    #we're done with this path.
    if(row == (len(m) - 1) and col == (len(m[0]) - 1)): #I hard coded the index pair into the function, but this can be changed

        s += "->" + str(m[row][col]) #concatenate the final node onto the running total
        print(s)
        return
        
    #If we overshot, no big deal, just don't count it among the solutions and return without printing.
    if(row > (len(m) - 1) or col > (len(m[0]) - 1)):
        return
        
    #recursively search each node below and to the right, and concatenate the current node to the running total.
    print_paths(row, col+1, s + "->" + str(m[row][col]))
    print_paths(row+1, col, s + "->" + str(m[row][col]))

print_paths()  # oletusarvoilla
print()
print_paths(0, 2)  # oik. ylh
print()
print_paths(1, 1)  # keskeltä