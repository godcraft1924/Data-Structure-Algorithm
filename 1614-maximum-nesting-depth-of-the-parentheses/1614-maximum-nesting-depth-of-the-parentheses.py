class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0 
        count  =0 
        stack = []
        for i in s :
            if i == "(":
                stack.append(i)
                count +=1
            elif i == ")":
                print(stack)
                maxi = max(count , maxi)
                count -= 1 
                stack.pop()
        return maxi


        