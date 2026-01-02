class Solution:
    def findMinArrowShots(self, b: List[List[int]]) -> int:
        b.sort(key= lambda x: x[1])
        ars, cur = 1, b[0][1]
        for s, e in b:
            if s > cur:
                ars += 1
                cur = e
        return ars