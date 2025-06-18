#DFS [Recursive] Solution - Time O(n) - Space O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))
    
#DFS [Iterative] Solution - Time O(n) - Space O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p, q]]
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            stack.append([p.left, q.left])
            stack.append([p.right, q.right])
        return True

#BFS [Iterative] Solution - Time O(n) - Space O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([q])
        q2 = deque([p])
        while q1 and q2:
            p = q1.popleft()
            q = q2.popleft()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            q1.append(p.left)
            q1.append(p.right)
            q2.append(q.left)
            q2.append(q.right)
        return True