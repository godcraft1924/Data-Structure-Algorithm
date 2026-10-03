class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxi = max(candies)
        result = [0]*len(candies)
        for i,c in enumerate (candies):
            if c+extraCandies  >= maxi:
                result[i] = True
            else:
                result[i] = False
        return result
                