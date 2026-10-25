
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = set()
        path = []
        number = [i for i in range(len(nums))]

        def solve():
            if len(path) == len(nums):
                result.add(tuple(path))
                return

            for i in number:
                if i not in used:
                    used.add(i)
                    path.append(nums[i])
                    solve()
                    path.pop()
                    used.remove(i)

        used = set()
        solve()

        return [list(p) for p in result]
