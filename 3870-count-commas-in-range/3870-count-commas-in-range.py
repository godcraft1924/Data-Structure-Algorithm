class Solution:
    def countCommas(self, n: int) -> int:
        if n/4 < 250: 
            return 0
        else: 
            # print("ss")
            return (n-1000)+1
        