class Solution:
    def countEven(self, num: int) -> int:


        def sumEven(n):
            sumi = 0 
            while n > 0: 
                remain = n%10
                sumi += remain 
                n  = n//10
            if sumi%2 ==  0 :
                return True
            else: 
                return False
        count = 0
        for i in range(1,num+1):
            print(i,sumEven(i))
            if sumEven(i) :
                count +=1 
        return count    
        