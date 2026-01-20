class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        def can_eat(piles, h, m):
            return sum([math.ceil(pile/m) for pile in piles]) <= h
        
        l, r = 1, max(piles)
        k = r
        
        while l<=r:
            m = (l+r) // 2
            if can_eat(piles, h, m):
                k = m
                r = m - 1
            else:
                l = m + 1
        return k