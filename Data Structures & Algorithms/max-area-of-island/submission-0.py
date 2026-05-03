class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(r,c):
            area = 1
            if (r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            area += (
                dfs(r+1, c) + 
                dfs(r-1, c) +
                dfs(r, c+1) +
                dfs(r, c-1)
                
            )
            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        return res