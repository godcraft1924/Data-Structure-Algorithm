class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        def getDigit(a):
            listi =[]
            while a > 0 :
                listi.append(a%10)
                a = a//10
            return listi[::-1]
        res = []
        for i in nums :
            res.extend(getDigit(i))
        return res
        