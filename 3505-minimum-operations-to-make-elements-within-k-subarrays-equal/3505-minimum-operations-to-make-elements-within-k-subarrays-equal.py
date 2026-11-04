class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= i & -i
        return ans

    def kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)

        while bit:
            nxt = idx + bit

            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]

            bit >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:

        # Coordinate compression
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        n = len(nums)
        m = len(vals)

        count = BIT(m)
        summ = BIT(m)

        total = 0
        costs = []

        # Calculate every window's median cost
        for i, num in enumerate(nums):

            r = rank[num]

            count.add(r, 1)
            summ.add(r, num)
            total += num

            # Remove outgoing element
            if i >= x:
                old = nums[i - x]
                r = rank[old]

                count.add(r, -1)
                summ.add(r, -old)
                total -= old

            if i >= x - 1:

                # Find median
                mid = count.kth((x + 1) // 2)
                median = vals[mid - 1]

                left_count = count.query(mid)
                left_sum = summ.query(mid)

                right_count = x - left_count
                right_sum = total - left_sum

                cost = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )

                costs.append(cost)

        # DP: minimum cost to select j non-overlapping windows
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Skip current position
                curr[i] = curr[i - 1]

                # Select window ending at i - 1
                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]