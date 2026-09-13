class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor  = 0
        for i in nums : 
            xor ^= i
        diff = xor & -xor
        a,b = 0,0
        for i in nums :
            if ( i & diff ==0 ):
                a ^= i
            else:
                b ^= i
        return [a,b]
            
        