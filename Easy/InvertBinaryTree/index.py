#Recursive DFS Solution - Time: O(n) Space: O(n)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
#Iterative DFS Solution - Time: O(n) Space: O(n)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

#BFS Solution - Time: O(n) Space: O(n)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root