#DFS [Recursive] Solution - Time O(n) - Space O(n)
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        return (self.sameTree(root.left, subRoot.left) and 
                self.sameTree(root.right, subRoot.right))