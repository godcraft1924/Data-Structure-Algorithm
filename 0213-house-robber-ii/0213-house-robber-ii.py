class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)== 1: 
            return nums[0]
        def solve(arr):
            prev_2= 0
            prev_1 = 0
            for i in range(0,len(arr)):
                skip = prev_1
                steal = prev_2 + arr[i]
                curr = max(skip,steal)
                prev_2 = prev_1
                prev_1 = curr
            return prev_1 
        first_skip  = solve(nums[1:])  
        first_steal = solve(nums[:-1])  
        return max(first_skip ,first_steal)