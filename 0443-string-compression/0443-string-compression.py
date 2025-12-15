class Solution:
    def compress(self, original: List[str]) -> int:
        p = 0
        res = []
        while p < len(original):
            num, cur = 0, original[p]

            while p < len(original) and original[p] == cur:
                num, p = num+1, p+1

            res.append(cur)
            if num > 1:
                for char in str(num):
                    res.append(char)
        original[:] = res

