class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if (nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            time += 1
        
        return time if fresh == 0 else -1