class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        element = len(nums)-1
        asc_count = 0 
        dsc_count = 0
        for i in range(1,n):
            if nums[i] == (nums[i-1]+1)%n:
                asc_count +=1 
            if nums[i-1] == (nums[i]+1)%n:
                dsc_count += 1 
        print(asc_count,dsc_count)
        if asc_count == element : 
            if nums[0] == 0 :
                return 0
            else:
               return  min(n-nums[0],nums[0]+2)
        if dsc_count == element :
            if nums[0] == element : 
                return 1 
            else: 
                return min(n-nums[-1]+1,(nums[0]+1)%n+1)

        else:
            return -1