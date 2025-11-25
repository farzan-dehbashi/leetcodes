class Solution(object):
    def twoSum(self, nums, target):
        seen = set()
        for i, num in enumerate(nums):
            if target - num in seen:
                return nums.index(target-num), i
            seen.add(num)
        return False
        