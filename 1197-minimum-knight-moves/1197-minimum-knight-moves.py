class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [
            (2,1), (2,-1), (-2,1), (-2,-1),
            (1,2), (-1,2), (1, -2), (-1, -2)
        ]

        q = deque([(0,0,0)])
        seen = {(0,0)}

        while q:
            cx, cy, steps = q.popleft()

            if (cx, cy) == (x, y):
                return steps

            for (dx, dy) in dirs:
                (nx, ny) = (cx+dx, cy+dy)
                if (nx, ny) not in seen and -300 <= nx <= 300 and -300 <= ny <= 300:
                    seen.add((nx, ny))
                    q.append((nx, ny, steps+1))
        return -1