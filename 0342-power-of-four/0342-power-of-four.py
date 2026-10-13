class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n >  0 and (n &  n-1 )== 0 :
            if bin(n)[2:].count("0")%2 == 0 :
                return True
            else:
                return False
        return False
