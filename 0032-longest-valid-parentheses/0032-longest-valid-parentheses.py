class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open = 0 
        close = 0 
        result = 0 
        for i in s : 
            if i == "(":
                open+=1
            else:
                close +=1 

            if open==close :
                result = max(result,open+close)
            elif close > open :
                open, close =  0,0 
        open, close =  0,0 
        for i in s[::-1]:
            print(i)
            if i == "(":
                open+=1
            else:
                close +=1 
            if open==close :
                result = max(result,open+close)
            elif open > close :
                open, close =  0,0
        return result
            