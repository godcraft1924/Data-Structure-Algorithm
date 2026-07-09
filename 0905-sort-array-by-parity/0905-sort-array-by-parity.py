class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start = 0
        end  = len(nums) -1 
        while start < end :
            x = nums[start]%2 
            y = nums[end]%2
            if  x != 0 and y ==0 :
                nums[start], nums[end]= nums[end], nums[start]
                start = start + 1
                end = end -1 
            if x == 0 :
                start =  start +1 
            if y != 0:
                end = end - 1 
        return nums 
            