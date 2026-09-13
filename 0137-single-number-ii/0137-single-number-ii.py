class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for k in range(32):
            temp = 1 << k 
            countOnes , countZeros = 0,0
            for   num in nums :
                if (num & temp ) == 0 :
                    countZeros  += 1 
                else:
                    countOnes += 1
            if countOnes % 3 == 1 :
                result = result | temp
        if result >= 2**31:
            result -= 2**32

        return result
