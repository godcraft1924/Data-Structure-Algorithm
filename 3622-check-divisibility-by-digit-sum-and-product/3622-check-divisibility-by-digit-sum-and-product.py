class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n_copy= n 
        sum = 0
        mul = 1 
        while n > 0 :
            remain = n%10
            sum += remain
            mul*= remain
            n = n//10
        # print(sum,mul,sum+mul)
        # print( n % (sum+mul))
        if n_copy% (sum+mul) == 0  :
            return True
        else: 
            return False