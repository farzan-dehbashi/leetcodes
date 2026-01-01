class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, sqs = 0, len(nums) - 1, []
        while l<=r:
            if abs(nums[l]) >= abs(nums[r]):
                sqs.append(nums[l] ** 2)
                l += 1
            else:
                sqs.append(nums[r] ** 2)
                r -= 1
        sqs.reverse()
        return sqs
