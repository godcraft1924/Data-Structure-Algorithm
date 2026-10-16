class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        sum = [0] * (n * 4)
        todo = [0] * (n * 4)

        def f(o, l, r, add):
            sum[o] += add * (r - l + 1)
            todo[o] += add

        def qry(o, l, r, L, R):
            if L <= l and r <= R:
                res = sum[o]
                f(o, l, r, 1)
                return res

            m = (l + r) // 2
            add = todo[o]
            if add:
                f(o * 2, l, m, add)
                f(o * 2 + 1, m + 1, r, add)
                todo[o] = 0

            res = 0
            if L <= m: res += qry(o * 2, l, m, L, R)
            if m < R:  res += qry(o * 2 + 1, m + 1, r, L, R)
            sum[o] = sum[o * 2] + sum[o * 2 + 1]
            return res

        res = s = 0
        last = {}
        for i, x in enumerate(nums, 1):
            j = last.get(x, 0)
            s += qry(1, 1, n, j + 1, i) * 2 + i - j
            res += s
            last[x] = i

        return res % 1000000007
# This code is copied pasted becuase the i do not know the concept of segement tree and i don't want to loose my 20 days sorry for myself 