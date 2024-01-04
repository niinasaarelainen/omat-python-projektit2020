from typing import List

m = []

def readfile():  
    f = open("data.txt", "r")         
    for rivi in f:
        rivi = rivi.strip()
        r = []
        for luku in rivi:
            r.append(int(luku))
        m.append(r)



def helper_4suuntaa(x, y, grid, cost):
    M, N = len(grid), len(grid[0])
    if x == M or y == N:
        return float('inf')
    elif cost[x][y] != -1:
        return cost[x][y]
    else:
        right, down = helper(x,y+1,grid,cost), helper(x+1,y,grid,cost), helper(x,y-1,grid,cost), helper(x-1,y,grid,cost)
        cost[x][y] = min(right, down) + grid[x][y]
    return cost[x][y]

def helper(x, y, grid, cost):
    M, N = len(grid), len(grid[0])
    if x == M or y == N:
        return float('inf')
    elif cost[x][y] != -1:
        return cost[x][y]
    else:
        right, down = helper(x,y+1,grid,cost), helper(x+1,y,grid,cost)
        cost[x][y] = min(right, down) + grid[x][y]
    return cost[x][y]
    
def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    M, N = len(grid), len(grid[0])
    cost = [[-1]*N for _ in range(M)]
    cost[M-1][N-1] = grid[M-1][N-1]
    return helper(0, 0, grid, cost)


readfile()
print(minPathSum(m) - m[0][0])