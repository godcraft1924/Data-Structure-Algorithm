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
        prev_2= 0
        prev_1 = 0
        for i in range(0,len(nums)):
            skip = prev_1
            steal = prev_2 + nums[i]
            curr = max(skip,steal)
            prev_2 = prev_1
            prev_1 = curr
        return((prev_1))
