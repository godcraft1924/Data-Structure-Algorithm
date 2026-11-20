from functools import cache
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        n  = len(nums)
        def findMethod(start,target,nums):


            right = len(nums)-1 
            left = start 
            ans   = -1 
            while left <= right : 
                mid = (left+right)//2 
                if nums[mid] == target : 
                    ans = mid  
                    right = mid - 1  
                   
                elif nums[mid] > target:
                    right = mid-1 
                elif nums[mid] < target :
                    left = mid+1 
            return ans  
        dp = [[0] * 2 for _ in range(n)]
        result = 1 
        for i in range(len(nums)-1,-1,-1):
            for j in range(2):
                currVal = nums[i] + j 
                length = 1 
                k = findMethod(i+1,currVal+1,nums)
                if k != -1 :
                    length  = max(length,1+dp[k][0])
                k = findMethod(i+1,currVal,nums)
                if k!= -1 :
                    length = max(length,1+ dp[k][1])
                dp[i][j] = length
                result  = max(result ,dp[i][j])
        print(dp)
        return result

 


        