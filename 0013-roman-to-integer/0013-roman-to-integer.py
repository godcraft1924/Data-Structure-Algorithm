class Solution:
    def romanToInt(self, s: str) -> int:
        key = {"I":1, "V":5 , "X":10 , 'L':50 , "C":100 , "D" : 500 ,"M":1000}
        i = 0 
        nums = 0 
        while i  < len(s):
            if  i+1<len(s) and key[s[i]]<key[s[i+1]]  :
                nums += key[s[i+1]] -key[s[i]]
                i = i+2
            else:
                nums +=  key[s[i]]
                i += 1
        return nums


