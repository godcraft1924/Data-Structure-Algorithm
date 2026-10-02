class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def solve(s,open,close,n):
            if len(s) == n*2 :
                result.append("".join(s))
                return
            if open<n:
                s.append("(")
                solve(s,open+1,close,n )
                s.pop()
            if close < open:
                s.append(")")
                solve(s,open,close+1,n)
                s.pop()


        solve([],0,0,n)
        return  result


        