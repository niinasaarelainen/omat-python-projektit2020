data = []

def readfile():  
    f = open("data_1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())



def uniquePaths(m: int, n: int) -> int:
    # dp[i][j] := the number of unique paths from (0, 0) to (i, j)
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]

readfile()
print(uniquePaths(len(data), len(data[0])))