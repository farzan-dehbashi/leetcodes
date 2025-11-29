class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q, fc, max_time = deque(), 0, 0
        dirs = [(-1,0), (1, 0), (0,-1), (0, 1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fc += 1
                elif grid[r][c] == 2:
                    q.append((r, c, 0))
        if fc == 0:
            return 0
        
        while q:
            r, c, t = q.popleft()
            max_time = max(max_time, t)

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    fc -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc, t+1))
        return max_time if fc == 0 else -1