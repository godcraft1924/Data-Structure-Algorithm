class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def solve(n):
            if n==0 or n ==1 :
                return  1 
            if n in  dp :
                return dp[n]
            dp[n] =  solve(n-1) + solve(n-2)
            print(dp)
            return dp[n]
        return solve(n)

        