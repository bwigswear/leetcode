class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        for x in range(r):
            for y in range(c):
                if matrix[x][y] == None: continue
                if matrix[x][y] == 0:
                    for row in range(r):
                        a = matrix[row][y]
                        if a == None: continue
                        if a != 0:
                            matrix[row][y] = None
                    for col in range(c):
                        a = matrix[x][col]
                        if a == None: continue
                        if a != 0:
                            matrix[x][col] = None
                    

        for x in range(r):
            for y in range(c):
                if matrix[x][y] == None:
                    matrix[x][y] = 0
