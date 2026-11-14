class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = float("inf")
        for i in range(len(nums)):
            total = 0 
            for j in range(i,len(nums)):
                total += nums[j]
                if l <= j - i + 1 <= r and total > 0:
                    res = min(res, total)
        return res if res != float("inf") else -1


        