from functools import cache
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)-1
        n = len(grid[0])-1
        if (m+n-1)%2 != 0:
            return False
        @cache
        def solve(i,j,opencount):
            if grid[i][j] =="(":
                opencount+=1
            else:
                opencount-=1
            if opencount <  0:
                return False 
            if (m -i) + (n-j )< opencount:
                return False
            if i==m and j == n :
                return opencount==0
            res = False
            if i+1 <= m :
                res = solve(i+1,j,opencount) or res
            if j+1 <= n and not res :
                res = solve(i,j+1,opencount) or res
            return res

        return solve(0,0,0)