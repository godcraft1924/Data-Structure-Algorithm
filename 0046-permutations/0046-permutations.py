class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        def solve():
            if len(path) == len(nums):
                result.append(path.copy())
            for  i in nums :
                if i not in  path :
                    path.append(i)
                    solve()
                    path.pop()
        solve()
        return result