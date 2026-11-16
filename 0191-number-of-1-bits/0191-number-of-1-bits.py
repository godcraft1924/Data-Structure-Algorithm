class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for k in range(32):  # Assuming a 32-bit integer
            if (n & (1 << k)) != 0:
                count += 1
        return count
        