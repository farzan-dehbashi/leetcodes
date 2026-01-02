class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols, rows, sqs = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                cur = board[r][c]
                if cur == '.':
                    continue
                if cur in rows[r] or cur in cols[c] or cur in sqs[(r//3, c//3)]:
                    return False
                rows[r].add(cur)
                cols[c].add(cur)
                sqs[(r//3, c//3)].add(cur)
        return True



                