class Solution:
    def countBits(self, n: int) -> list[int]:
        res =[]
        for i in range(n+1):
            count = 0 
            while i > 0:
                count += (i%2)
                i//=2 
            # print(count)
            res.append(count)
        return res


        