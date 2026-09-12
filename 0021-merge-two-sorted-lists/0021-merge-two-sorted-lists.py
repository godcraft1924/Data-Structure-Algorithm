class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        headA = list1
        headB = list2

        dummy = ListNode()
        current = dummy

        while headA and headB:

            if headA.val <= headB.val:
                current.next = headA
                headA = headA.next
            else:
                current.next = headB
                headB = headB.next

            current = current.next

        if headA:
            current.next = headA

        if headB:
            current.next = headB

        return dummy.next