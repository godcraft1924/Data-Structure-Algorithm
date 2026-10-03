class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        num = nums.copy()
        nums.sort()
        print(nums)
        result = []
        for i in num:
            result.append(nums.index(i))
        return result
        