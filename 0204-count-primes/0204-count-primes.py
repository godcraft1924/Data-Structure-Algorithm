class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        arr = [True]*n
        for i in range(2,int(n**(1/2))+1):
            if arr[i]:
                for j in range(i*i,n,i):
                    arr[j] = False
        arr[0] , arr[1] = False, False
        
        return sum(arr)


        