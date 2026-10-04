class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == "*":
                star.append(i)
            else:
                # print(i,stack)
                if stack:
                    stack.pop()
                else:
                    if star and i>star[-1]:
                        star.pop()
                    else:
                        # print("1")
                        return False 
        while star and stack and stack[-1] < star[-1]:
            star.pop()
            stack.pop()
        if not stack:
            return True
        else:
            return False

        