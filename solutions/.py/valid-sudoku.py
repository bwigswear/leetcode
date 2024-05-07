class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = 9
        cols = 9

        for row in board:
            a = set()
            for num in row:
                if num in a: return False
                if num != '.': a.add(num)

        for i in range(cols):
            a = set()
            for j in range(rows):
                num = board[j][i]
                if num in a: return False
                if num != '.': a.add(num)

        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                a = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        num = board[k][l]
                        if num in a: return False
                        if num != '.': a.add(num)

        return True