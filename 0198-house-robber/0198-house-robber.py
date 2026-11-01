class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [-1]*len(nums)

        def solve(i):
            if i > len(nums)-1:
                return 0
            if dp[i] != -1:
                return dp[i]
            steal = nums[i]+ solve(i+2)
            skip  =  solve(i+1)
            # print(skip,steal)
            dp[i] = max(steal,skip)
            return dp[i]
        return solve(0)
       