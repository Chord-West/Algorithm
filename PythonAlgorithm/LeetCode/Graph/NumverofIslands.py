from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(sx, sy):
            visited[sy][sx] = 1
            q = deque([(sx, sy)])
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[ny][nx] == '1' and visited[ny][nx] == 0:
                            visited[ny][nx] = 1
                            q.append((nx, ny))

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        visited = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    bfs(j, i)
                    cnt += 1

        return cnt