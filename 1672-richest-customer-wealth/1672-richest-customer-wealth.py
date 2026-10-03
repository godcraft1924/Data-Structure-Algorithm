class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxi = 0
        for i in accounts :
            maxi = max(maxi,sum(i))
        return maxi
        