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
        

#BFS [Iterative] Solution - Time O(n) - Space O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: