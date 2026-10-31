from functools import cache
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9+7
        m = len(grid)-1
        n= len(grid[0])-1
        @cache
        def solve(i,j,cameFrom):
            if i==m and j==n :
                return 1 
            if i < 0 or i> m or j<0 or j> n:
                return 0 
            
            if grid[i][j] == 0 :
                total = 0
                total+= solve(i+1,j,"down")
                total+= solve(i,j+1,"right")
                return total %MOD
            else:
                if cameFrom == 'down':
                    return solve(i,j+1,"right")
                else: 
                    return solve(i+1,j,"down")
        return solve(0,0,"")