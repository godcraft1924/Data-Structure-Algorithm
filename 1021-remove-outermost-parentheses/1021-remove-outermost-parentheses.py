class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0 
        new_str = ""
        for i in range(len(s)) : 
            if s[i] =="(":
                count+= 1
                if count != 1 :
                    new_str += s[i]
                     
            else:
                count -=1
                if count != 0 :
                    new_str +=s[i]

            # print(s[i],count,new_str)

        return new_str