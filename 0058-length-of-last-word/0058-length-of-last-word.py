class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newList = s.split()
        return len(newList[-1])
        