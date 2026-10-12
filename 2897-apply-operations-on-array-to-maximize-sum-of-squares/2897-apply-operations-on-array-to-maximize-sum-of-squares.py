class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = (10**9)+7
        count = [0]*32
        result = 0 
        for i in nums :
             for j in range(31):
               if (i & (1 << j)) != 0:
                    count[j] +=1 
        while k!=0 :
            curr = 0 
            for j in range(31):
                if count[j] >  0 :
                    count[j] -=1 
                    curr = curr | 1<<j
            k-=1
            result = result + (curr*curr)
        return result%mod
        