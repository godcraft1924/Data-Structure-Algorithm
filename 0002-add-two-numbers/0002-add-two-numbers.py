class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        newNode = ListNode(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = LinkedList()
        temp1, temp2 = l1, l2
        carry = 0
        while temp1 or temp2:
            x = temp1.val if temp1 else 0
            y = temp2.val if temp2 else 0
            total = x + y + carry
            carry, digit = divmod(total, 10)
            ans.insert(digit)
            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
        if carry:
            ans.insert(carry)
        return ans.head