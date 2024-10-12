def isCorner(i, j, M, N):
    if((i == 0 and j == 0) or (i == 0 and j == N-1) or (i == M-1 and j == N-1) or (i == M-1 and j == 0)):
        return True
    return False
 
# Function to check if the index is
# within the matrix boundary.
def isValid(i, j, M, N):
    if(i < 0 or i >= M or j < 0 or j >= N):
        return False
    return True
 
# Recursive helper function
def solve(i, j, M, N, Dir, maze, t, ans):
   
    # If any corner is reached push the
    # string t into ans and return
    if(i == 0 and j== 1):
        ans.append(t)
        return
       
    # For all the four directions
    for k in range(4):
       
      # The new ith index
        x = i + Dir[k][0]
         
        # The new jth index
        y = j + Dir[k][1]
         
        # The direction R/L/U/D
        c = Dir[k][2]
         
         # If the new cell is within the
        # matrix boundary and it is not
        # previously visited in same path
        if(isValid(x, y, M, N) and maze[x][y] == 1):
           
          # mark the new cell visited
            maze[x][y] = 0
             
            # Store the direction
            t += c
            solve(x, y, M, N, Dir, maze, t, ans)
             
             # Backtrack to explore
            # other paths
            t = t[: len(t)-1]
            maze[x][y] = 1
    return
 
# Function to find all possible paths
def possiblePaths(src, maze):
   
     # Create a direction  array for all
    # the four directions
    Dir = [[-1, 0, 'U'], [0, 1, 'R'], [1, 0, 'D'], [0, -1, 'L']]
     
    # stores the result  
    temp = ""
    ans = []
    solve(src[0], src[1], len(maze), len(maze[0]), Dir, maze, temp, ans)
    return ans

 
# Initialise variable
maze = [[1, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1]]
src = [0, 0]
 
# function call
paths = possiblePaths(src, maze)
 
# Print the result
if(len(paths) == 0):
    print("No Possible Paths")
else:
    for i in paths:
        print(i)