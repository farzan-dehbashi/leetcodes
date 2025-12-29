class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        for r in range(len(m)):
            for c in range(r+1, len(m[0])):
                m[r][c], m[c][r] = m[c][r], m[r][c]
        
        for r in range(len(m)):
            m[r].reverse()

        return m