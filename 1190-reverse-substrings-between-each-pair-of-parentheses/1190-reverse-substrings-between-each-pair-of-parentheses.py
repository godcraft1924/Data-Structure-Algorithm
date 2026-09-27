class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack  = []
        reverse_string = ""
        for i in s : 
            if i =="(":
                stack.append(i)
            elif i == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                for ch in temp:
                    stack.append(ch)
                               
            else:
                stack.append(i)

        return "".join(stack)