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
        print(m[row][col])
        
        if ( col+1 < len(m[0]) and m[row][col+1] - m[row][col] in [0, 1, -1] ):
            print("1", m[row][col+1] - m[row][col] )
            print_paths_oma(row, col+1, s + "," + str(m[row][col]))

        
        if ( col-1 >= 0 and m[row][col] - m[row][col-1] in [0, 1, -1] ):
            print("2", m[row][col] - m[row][col-1] )
            print_paths_oma(row, col-1, s + "," + str(m[row][col]))

        
        if ( row+1 < len(m[0]) and m[row+1][col] - m[row][col] in [0, 1, -1] ):
            print("3",  m[row+1][col] - m[row][col])
            print_paths_oma(row+1, col, s + "," + str(m[row][col]))

        
        if ( row-1  >= 0 and m[row-1][col] - m[row][col] in [0, 1, -1] ):
            print("4",  m[row-1][col] - m[row][col])
            print_paths_oma(row-1, col, s + "," + str(m[row][col]))