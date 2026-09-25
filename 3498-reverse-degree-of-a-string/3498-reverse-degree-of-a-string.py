class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0 
        for i in range(len(s)) :
            sum += (26-(ord(s[i])-ord("a"))) * (i+1)
        return  sum