class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        m = set()
        for i in nums:
            print(i)
            if i not in m :
                m.add(i)
            else:
                return i
        