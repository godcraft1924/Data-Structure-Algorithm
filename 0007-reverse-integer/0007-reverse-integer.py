class Solution:
    def reverse(self, x: int) -> int:
        negative = False 
        if x < 0 :
            negative =True
            x = abs(x)     
        # reverse = 0 
        # while x > 0 :
        #     digit = x % 10 
        #     reverse = reverse*10 + digit
        #     x = x //10 
        # if negative :
        #     reverse =  reverse * -1 
        str_x = str(x)
        reverse = int(str_x[::-1])
        if negative:
            reverse = reverse* -1 
        if reverse > -2**31 and reverse < 2**31 :
            return reverse 
        else:
            return 0
