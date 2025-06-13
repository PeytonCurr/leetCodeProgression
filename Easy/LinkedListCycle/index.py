#Iterative [Hashmap] Solution - Time: O(n) Space: O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        oldNodes = set()
        while head:
            if head.next in oldNodes:
                return True
            oldNodes.add(head.next)
            head = head.next
        return False

#Optimal Solution [Two Pointers] - Time: O(n) Space: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastP = head
        while fastP and fastP.next:
            head = head.next
            fastP = fastP.next.next
            if fastP == head:
                return True
        return False