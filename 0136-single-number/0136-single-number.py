class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mul = 0
        for i  in nums:
            mul ^= i
        return mul
        