class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        c, cur = 0, 1
        while c < k:
            if not cur in nums_set:
                c += 1
            cur += 1
        return cur - 1

    
        