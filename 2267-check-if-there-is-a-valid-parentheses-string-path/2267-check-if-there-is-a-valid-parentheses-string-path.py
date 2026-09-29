
from functools import cache
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        m = len(grid) - 1
        n = len(grid[0]) - 1
        @cache
        def solve(i, j, openCount):

            if grid[i][j] == "(":
                openCount += 1
            else:
                openCount -= 1

            if openCount < 0:
                return False

            remaining = (m - i) + (n - j)

            if openCount > remaining:
                return False
            if i == m and j == n:
                return openCount == 0
            res = False

            if i + 1 <= m:
                res =  solve(i + 1, j, openCount) or res

            if j + 1 <= n and not res:
                res=  solve(i, j + 1, openCount) or res 
            return res

        if grid[0][0] == ")" or grid[m][n] == "(":
            return False

        if (m + n + 1) % 2 == 1:
            return False

        return solve(0, 0, 0)