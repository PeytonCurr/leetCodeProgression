class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev