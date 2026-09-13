class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        xor = 0 
        seen = 0
        for   i  in nums :
            if (seen & (1<<i)) == 0:
                seen |= 1<<i
            else:
                xor^=i 
        print(bin(seen))
        return xor
