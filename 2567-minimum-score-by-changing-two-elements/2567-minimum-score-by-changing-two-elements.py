class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        case2 = abs(nums[2]-nums[-1])
        case1 = abs(nums[1]-nums[-2])
        case3 = abs(nums[0]-nums[-3])
        return min(case1, case2, case3)
    
        