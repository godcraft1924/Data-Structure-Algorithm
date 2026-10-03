class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        maximum = 0 
        count = 0 
        ending = -1
        for i in range(0,len(s)):
            # print(stack)
            if s[i] =="(" :
                stack.append([s[i],i])
            else:
                if stack:
                    if stack[-1][0] == "(" :
                        stack.pop()
                        if stack:
                            count = i - stack[-1][1]
                        else:
                            count = i - ending
                        maximum = max(count,maximum)
                    else:
                        # # print('stack is clear', stack)
                        # stack.clear()
                        # # print('stack is cleared', stack)
                        # ending = i
                        pass
                else:
                    ending = i 
                    # starting = i+i
        
        return maximum




        