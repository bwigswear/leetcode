class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited =[[0 for y in x] for x in grid]
        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        def bfs(x, y):
            queue = []
            queue.append((x, y))
            while len(queue) > 0:
                r, c = queue.pop(0)
                if r < 0 or r >= rows or c < 0 or c >= columns:
                    continue
                if visited[r][c] == 0:
                    visited[r][c] = 1
                    if grid[r][c] == '1':
                        queue.append((r - 1, c))
                        queue.append((r + 1, c))
                        queue.append((r, c + 1))
                        queue.append((r, c - 1))


        for i in range(rows):
            for j in range(columns):
                if visited[i][j] == 0:
                    if grid[i][j] == '1':
                        islands+=1
                        bfs(i, j)
                    else:
                        visited[i][j] = 1

        return islands