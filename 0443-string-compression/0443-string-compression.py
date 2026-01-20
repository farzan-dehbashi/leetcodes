class Solution:
    def compress(self, original: List[str]) -> int:
        w = r = 0
        while r < len(original):
            cur = original[r]
            c = 0

            while r < len(original) and original[r] == cur:
                c, r = c+1, r+1
            
            original[w] = cur
            w += 1

            if c > 1:
                for digit in str(c):
                    original[w] = digit
                    w += 1
        return w

