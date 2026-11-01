class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)== 1: 
            return nums[0]
        def solve(arr):
            dp = [-1]*(len(arr)+1)
            dp[0] = 0
            dp[1] = arr[0]
            for i in range(2,len(arr)+1):
                steal = arr[i-1]+ dp[i-2]
                skip = dp[i-1]   
                dp[i] = max(steal ,skip)
            return dp[-1]   
            dp = [-1] * (len(nums)+1)
        first_skip  = solve(nums[1:])  
        first_steal = solve(nums[:-1])  
        return max(first_skip ,first_steal)