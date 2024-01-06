class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        currentNode = head

        while currentNode:
            if currentNode in hashset:
                return True
            hashset.add(currentNode)
            currentNode = currentNode.next
        return False
# Solution Time: O(n) & Mem: O(n)