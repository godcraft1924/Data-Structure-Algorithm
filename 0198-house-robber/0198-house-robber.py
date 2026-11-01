class Solution:
    def rob(self, nums: list[int]) -> int:
        # Top up version 
        # dp = [-1]*len(nums)

        # def solve(i):
        #     if i > len(nums)-1:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     steal = nums[i]+ solve(i+2)
        #     skip  =  solve(i+1)
        #     # print(skip,steal)
        #     dp[i] = max(steal,skip)
        #     return dp[i]
        # return solve(0)
    #  bottom down version 
        dp = [-1] * (len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2,len(nums)+1):
            steal = nums[i-1]+ dp[i-2]
            skip = dp[i-1]
            dp[i] = max(steal,skip)
        return(dp[-1])
