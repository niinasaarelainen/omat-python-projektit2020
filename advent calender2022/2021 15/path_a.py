from typing import List

m = []
ind = []
min_summa = 900
summa_liaaniso = 910

def readfile():  
    f = open("data_1.txt", "r")         
    for rivi in f:
        rivi = rivi.strip()
        r = []
        for luku in rivi:
            r.append(int(luku))
        m.append(r)

def muodosta_ind():
    nro = 1
    for rivi in m:
        r = []
        for luku in rivi:
            r.append(nro)
            nro += 1
        ind.append(r)


def print_paths(row=0, col=0, sum = 0, monesko = 0):
    global min_summa
    #this is the recursive base case, if we're at the bottom right corner after this traversal, 
    #we're done with this path.
    if(row == (len(m) - 1) and col == (len(m[0]) - 1)): #I hard coded the index pair into the function, but this can be changed

        sum += m[row][col] #concatenate the final node onto the running total
        if sum < min_summa:
            min_summa = sum
        return
        
    #If we overshot, no big deal, just don't count it among the solutions and return without printing.
    if(row > (len(m) - 1) or col > (len(m[0]) - 1)):
        return
        
    #recursively search each node below and to the right, and concatenate the current node to the running total.
    if sum < min_summa or 9 != m[row][col] or 8 != m[row][col]:
        print_paths(row, col+1, sum + m[row][col], monesko+1)
        print_paths(row+1, col, sum + m[row][col], monesko+1)
    return


def min_path_sum(grid: List[List[int]]) -> int:
   
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])

    # column's 0th row sum
    for j in range(1, n):
        grid[0][j] = grid[0][j-1] + grid[0][j]

    # row's 0th column sum
    for i in range(1, m):
        grid[i][0] = grid[i-1][0] + grid[i][0]

    # computing rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

    
    return grid[-1][-1]


readfile()
print(m)
#muodosta_ind()
#reitin_pit = len(ind[0]) + len(ind)
#print(reitin_pit)
#print_paths()
#print(min_summa- m[0][0])  # 900 too high
print(min_path_sum(m) - m[0][0])  # top-left ei ole mukana 

