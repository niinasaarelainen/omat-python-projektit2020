class NoOfPaths:
    def count(self, arrA, row, col):
        # Base case
        # Check if the last row or column is reached since after that only one path
        # is possible to reach the bottom right corner.
        if row == len(arrA) - 1 or col == len(arrA[0]) - 1:
            return 1
        return self.count(arrA, row + 1, col) + self.count(arrA, row, col + 1)


    def reitit(self, arrA, row, col, tulos):
        # Base case
        # Check if the last row or column is reached since after that only one path
        # is possible to reach the bottom right corner.
        if row == len(arrA) - 1 or col == len(arrA[0]) - 1:        # REITIT !!!!!!!!!!!!!!!
            if arrA[row][col] not in tulos:
                tulos.append(arrA[row][col])
            return tulos
        return self.reitit(arrA, row + 1, col, tulos) + self.reitit(arrA, row, col + 1, tulos)

def foo(a): 
        [print(*(a[0][j:i+1] + a[1][i:]), sep="") for j in range(3) for i in range(j, 3)]
    

if __name__ == "__main__":
    arrA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]#, [10, 11, 12]]
    no_of_paths = NoOfPaths()
    print("No Of Paths (Recursion):", no_of_paths.count(arrA, 0, 0))
    print("Reitit (Recursion):", no_of_paths.reitit(arrA, 0, 0, []))

    foo(arrA)
    