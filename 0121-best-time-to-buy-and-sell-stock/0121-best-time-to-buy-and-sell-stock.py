class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf, minPrice = 0, float('inf')
        for price in prices:
            maxProf = max(price - minPrice, maxProf)
            minPrice = min(minPrice, price)
        return maxProf


