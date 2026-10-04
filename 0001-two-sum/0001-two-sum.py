class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i in range(len(nums)) : 
            minus = target - nums[i] 
            if minus in dict :
                return [i,dict[minus]]
            dict[nums[i]] = i 
        