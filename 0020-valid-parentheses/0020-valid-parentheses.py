class Solution:
    def isValid(self, s: str) -> bool:
        stack = [ ]
        keys = {"(":")","{":"}","[":"]"}
        for i in s : 
            if i in keys :
                stack.append(i)
            else:
                if stack:
                    if keys[stack[-1]]== i:
                        stack.pop()
                    else:
                        return False
                
                else:
                    return False    
        if stack: 
            return False
        else:
            return True    