class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans,even,odd = 0,0,0
        MOD = 10**9 +7
        for i in arr :
            if i %2 :
                even,odd = odd ,even +1 
            else:
                even += 1 
            ans += odd 
        return ans%MOD

        