class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicto = {}
        for i in range (len(nums)):
            complement = target-nums[i]
            if complement in dicto:
                return [dicto[complement],i]
            else:
                dicto[nums[i]] = i 