class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i,c in enumerate(s):
            if c == "(":
                stack.append([c,i])
            elif c == "*":
                star.append([c,i])
            else:
                # print(i,stack)
                if stack:
                    stack.pop()
                else:
                    if star and i>star[-1][1]:
                        star.pop()
                    else:
                        print("1")
                        return False
        if not  stack :
            print("1")
            return True
        elif not star :
            print("2")
            return False 

        len_stack = len(stack)
        len_star= len(star)
        for i in range(min(len_stack,len_star)):
            print(stack, star)
            if stack[-1][1] < star[-1][1]:
                stack.pop()
                star.pop()
            else:
                print("3")
                return False
        if not stack:
            print("2")
            return True
        else:
            return False

        