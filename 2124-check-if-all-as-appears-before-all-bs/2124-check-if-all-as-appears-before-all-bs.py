class Solution:
    def checkString(self, s: str) -> bool:
        a_index = float("inf")
        b_index = float("inf")
        for i in range(1,len(s)+1):
            if s[i-1] == "a":
                a_index = i-1
            if s[-(i)] == "b":
                b_index = i 
                # print(-i)
        if a_index == float("inf")  or b_index == float("inf"):
            return True
        if a_index < (len(s)- b_index) :
            return  True
        else: 
            return False
        