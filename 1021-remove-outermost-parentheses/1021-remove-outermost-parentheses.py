#  we can use str but using string in for loop create new str reassiging again which is slow so i am using list to make fast
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0 
        new_str = []
        for i in range(len(s)) : 
            if s[i] =="(":
                count+= 1
                if count != 1 :
                    new_str.append(s[i])
                     
            else:
                count -=1
                if count != 0 :
                    new_str.append(s[i])

            # print(s[i],count,new_str)

        return "".join(new_str)