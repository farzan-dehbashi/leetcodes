class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            sumation = nums[l] + nums[r]
            if sumation == target:
                return [l+1, r+1]
            elif sumation < target:
                l += 1
            else:
                r -= 1
