class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res, counts = 0, collections.defaultdict(int)
        for num in nums:
            res += counts[num-k] + counts[num+k]
            counts[num] += 1
        return res
        