class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # if len(nums) == 1 :
        #     return nums[0]
        currSum  = 0 
        maxSum =nums[0] 
        for  i in nums :
            currSum += i
            maxSum  = max(maxSum, currSum)
            if currSum < 0 :
                currSum = 0 
        return maxSum