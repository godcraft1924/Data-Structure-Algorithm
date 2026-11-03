class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sumi= sum(nums)
        maxi= max(nums)
        return (len(nums)*maxi) - sumi