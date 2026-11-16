# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        tmp = []
        temp = head 
        while temp :
            tmp.append(temp.val)
            temp = temp.next
        res = 0 
        for i in range(0,len(tmp)):
            if tmp[i] == 1 :
                k = len(tmp)-i-1
                print(k,1<<k) 
                res |= 1<<k
        return res 