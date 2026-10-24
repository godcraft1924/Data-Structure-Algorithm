class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        path = []
        result = []
        nums  =  [ i for i in range(1,n+1)]
        def solve(start):
            if len(path) ==  k :
                result.append(path.copy())
                return

            for num in range(start,n):
                if nums[num] not in path:
                    path.append(nums[num])
                    solve(num+1)
                    path.pop()

        solve(0)
        return result
