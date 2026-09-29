class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        m = len(grid) - 1
        n = len(grid[0]) - 1
        memo = {}

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

            if (i, j, openCount) in memo:
                return memo[(i, j, openCount)]

            if i + 1 <= m:
                if solve(i + 1, j, openCount):
                    memo[(i, j, openCount)] = True
                    return True

            if j + 1 <= n:
                if solve(i, j + 1, openCount):
                    memo[(i, j, openCount)] = True
                    return True

            memo[(i, j, openCount)] = False
            return False

        if grid[0][0] == ")" or grid[m][n] == "(":
            return False

        if (m + n + 1) % 2 == 1:
            return False

        return solve(0, 0, 0)