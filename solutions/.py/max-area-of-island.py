class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[0 for y in x] for x in grid]
        max = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            nonlocal max
            queue = []
            queue.append((r, c))
            size = 0
            while len(queue) > 0:
                x, y = queue.pop(0)
                if x < 0 or x > rows - 1 or y < 0 or y > cols - 1: continue
                if visited[x][y] == 0:
                    visited[x][y] = 1
                    if grid[x][y] == 1:
                        size+=1
                        queue.append((x + 1, y))
                        queue.append((x - 1, y))
                        queue.append((x, y + 1))
                        queue.append((x, y - 1))
            if size > max: max = size



        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0:
                    if grid[r][c] == 1:
                        bfs(r, c)
                    else:
                        visited[r][c] = 1
                
        return max