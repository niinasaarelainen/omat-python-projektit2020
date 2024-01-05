from typing import List

m = []

def readfile():  
    f = open("data_oma2.txt", "r")       # oikea vastaus 21, mennään myös ylös ja vas.   
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
        right, down, up, left = helper(x,y+1,grid,cost), helper(x+1,y,grid,cost), helper(x,y-1,grid,cost), helper(x-1,y,grid,cost)
        cost[x][y] = min(right, left, down, up) + grid[x][y]
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
    return helper_4suuntaa(0, 0, grid, cost)    # poista 4suuntaa ??




readfile()
print(minPathSum(m) - m[0][0])