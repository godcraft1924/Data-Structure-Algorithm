class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)) : 
            sum  = 0 
            j = nums[i]
            while j>0 :
                remain = j%10
                sum += remain 
                j  = j//10
            if sum == i :
                return i
        else:
            return -1