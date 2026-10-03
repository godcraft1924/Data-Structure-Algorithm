class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s= []
        sumi = 0
        for  i in nums:
            sumi+= i
            s.append(sumi)
        return s