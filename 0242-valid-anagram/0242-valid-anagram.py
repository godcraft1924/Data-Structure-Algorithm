class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chr  = [0]* 26
        for i in s :
            chr[ord(i)-ord('a')] += 1 
        for i in t: 
            chr[ord(i)-ord('a')] -= 1 
        return all(x == 0 for x in chr)

        