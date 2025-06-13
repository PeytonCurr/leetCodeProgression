#Optimal Solution [Reverse and Merge] - Time: O(n) Space: O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sp, fp = head, head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

        beginL2 = sp.next
        prev = sp.next = None

        while beginL2: 
            tmp = beginL2.next
            beginL2.next = prev
            prev = beginL2
            beginL2 = tmp
        
        curr = head
        while prev:
            tmp, tmp2 = curr.next, prev.next
            curr.next = prev
            prev.next = tmp
            curr, prev = tmp, tmp2