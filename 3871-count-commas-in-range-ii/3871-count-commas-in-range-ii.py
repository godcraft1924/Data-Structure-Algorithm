class Solution:
    def countCommas(self, n: int) -> int:
        u  = 0 
        x = 1000
        while x <= n:
            u += (n-x)+1
            x *= 1000
        return u