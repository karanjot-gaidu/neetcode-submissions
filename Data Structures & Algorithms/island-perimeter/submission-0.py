class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1
            
            if (r, c) in visited:
                return 0
            
            visited.add((r,c))

            perimeter = dfs(r, c+1) + dfs(r+1, c) + dfs(r, c-1) + dfs(r-1, c)
            return perimeter
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r, c)
        return 0