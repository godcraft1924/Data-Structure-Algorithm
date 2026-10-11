class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        for i in range(1,len(nums)+1):
            # print(i)
            if len(nums)%i == 0:
                # print(i,"divide")
                sum += nums[i-1]**2
        return sum