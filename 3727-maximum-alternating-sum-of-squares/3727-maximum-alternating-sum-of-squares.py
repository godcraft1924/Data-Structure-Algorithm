class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] *= nums[i]
        nums.sort()
        # -sum(nums[:n//2]) smaller number in odd index
        #  sum(nums[n//2:]) positive number in even index
        return  -sum(nums[:n//2]) + sum(nums[n//2:])
        