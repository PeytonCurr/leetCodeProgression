class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowP = head
        fastP = head
        while fastP:
            slowP = slowP.next
            fastP = fastP.next
            if fastP:
                fastP = fastP.next
            else:
                return False
            if slowP == fastP:
                return True
        return False
# Solution Time: O(n) & Mem: O(1)