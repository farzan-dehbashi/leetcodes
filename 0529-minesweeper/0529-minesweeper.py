class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        ROWS, COLS = len(board), len(board[0])
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        dirs = [(-1,-1), (-1,0), (-1,1), (0, -1), (0,1), (1,-1), (1, 0), (1,1)]

        def count_mines(r, c):
            nonlocal ROWS, COLS
            count = 0
            for dr, dc in dirs:
                if 0<= r+dr < ROWS and 0 <= c+dc < COLS and board[r+dr][c+dc] == 'M':
                    count += 1
            return count

        def dfs(r, c):
            nonlocal ROWS, COLS
            if not (0<=r<ROWS and 0<=c<COLS) or not board[r][c] == 'E':
                return 
            mine_c = count_mines(r,c)
            if mine_c > 0:
                board[r][c] = str(mine_c)
            else:
                board[r][c] = 'B'
                for dr, dc in dirs:
                    dfs(r+dr, c+dc)
        dfs(r,c)
        return board

