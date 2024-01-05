from functools import cmp_to_key
 

grid = []

def readfile():  
    f = open("data.txt", "r")         
    for rivi in f:
        rivi = rivi.strip()
        r = []
        for luku in rivi:
            r.append(int(luku))
        grid.append(r)


 
def mycmp(a,b):
     
    if (a.distance == b.distance):
        if (a.x != b.x):
            return (a.x - b.x)
        else:
            return (a.y - b.y)
    return (a.distance - b.distance)
 
# structure for information of each cell
class cell:
 
    def __init__(self,x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance
 
# Utility method to check whether a point is
# inside the grid or not
def isInsideGrid(i, j):
    return (i >= 0 and i < ROW and j >= 0 and j < COL)
 
# Method returns minimum cost to reach bottom
# right from top left
def shortest(grid, row, col):
    dis = [[0 for i in range(col)]for j in range(row)]
 
    # initializing distance array by INT_MAX
    for i in range(row):
        for j in range(col):
            dis[i][j] = 1000000000
 
    # direction arrays for simplification of getting
    # neighbour
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
 
    st = []
 
    # insert (0, 0) cell with 0 distance
    st.append(cell(0, 0, 0))
 
    # initialize distance of (0, 0) with its grid value
    dis[0][0] = grid[0][0]
 
    # loop for standard dijkstra's algorithm
    while (len(st)!=0):
 
        # get the cell with minimum distance and delete
        # it from the set
        k = st[0]
        st = st[1:]
 
        # looping through all neighbours
        for i in range(4):
 
            x = k.x + dx[i]
            y = k.y + dy[i]
 
            # if not inside boundary, ignore them
            if (isInsideGrid(x, y) == 0):
                continue
 
            # If distance from current cell is smaller, then
            # update distance of neighbour cell
            if (dis[x][y] > dis[k.x][k.y] + grid[x][y]):
                # update the distance and insert new updated
                # cell in set
                dis[x][y] = dis[k.x][k.y] + grid[x][y]
                st.append(cell(x, y, dis[x][y]))
 
        st.sort(key=cmp_to_key(mycmp))
 
    # uncomment below code to print distance
    # of each cell from (0, 0)
 
    # for i in range(row):
    #     for j in range(col):
    #         print(dis[i][j] ,end= " ")
    #     print()
 
    # dis[row - 1][col - 1] will represent final
    # distance of bottom right cell from top left cell
    return dis[row - 1][col - 1]
 
# Driver code to test above methods
 
"""
grid = [[31, 100, 65, 12, 18], 
[10, 13, 47, 157, 6], 
[100, 113, 174, 11, 33], 
[88, 124, 41, 20, 140],
[99, 32, 111, 41, 20]] """


readfile()
ROW = len(grid)
COL = len(grid[0])

print(shortest(grid, ROW, COL) - grid[0][0])