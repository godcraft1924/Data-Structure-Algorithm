from functools import cache
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        n  = len(nums)
        def findMethod(start,target,nums):
            right = len(nums)-1 
            left = start 
            ans   =-1 
            while left <= right : 
                mid = (left+right)//2 
                if nums[mid] == target : 
                    ans = mid  # Save this index
                    right = mid - 1  
                   
                elif nums[mid] > target:
                    right = mid-1 
                elif nums[mid] < target :
                    left = mid+1 
            return ans  


        @cache 
        def solve(i,inc):
            currVal = nums[i] + inc
            length = 1 
            j  = findMethod(i+1,currVal+1,nums)
            if (j != -1 ):
                length = max(length, 1 + solve(j,0))
            j = findMethod(i+1,currVal,nums)
            if (j != -1 ):
                length = max(length, 1 + solve(j,1))
            return length
        result  =1 
        for i  in range(len(nums)):
            result = max(result , solve(i,1),solve(i,0))
        return result
 


        