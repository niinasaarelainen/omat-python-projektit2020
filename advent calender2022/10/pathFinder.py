from typing import List

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


grid = [
    [1, 3, 1], 
    [1, 5, 1],
    [4, 2, 1]
]
grid1 = [
    [1, 2, 3], 
    [4, 5, 6]
]

print(min_path_sum(grid)) # prints 7
print(min_path_sum(grid1)) # prints 12