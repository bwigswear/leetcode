class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def protect(x, y):
            if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                return
            if board[x][y] == 'O':
                board[x][y] = 'P'
                protect(x - 1, y)
                protect(x, y - 1)
                protect(x + 1, y)
                protect(x, y + 1)
        for x in range(0, rows):
            if board[x][0] == 'O':
                board[x][0] = 'P'
                protect(x, 1)
            if board[x][cols - 1] == 'O':
                board[x][cols - 1] = 'P'
                protect(x, cols - 2)
        for y in range(0, cols):
            if board[0][y] == 'O':
                board[0][y] = 'P'
                protect(1, y)
            if board[rows - 1][y] == 'O':
                board[rows - 1][y] = 'P'
                protect(rows - 2, y)

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'P':
                    board[x][y] = 'O'