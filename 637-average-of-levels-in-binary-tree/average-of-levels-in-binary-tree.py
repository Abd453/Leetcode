# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = deque([root])
        result = []
        
        while queue:
            length = len(queue)
            sum1 = 0
            
            for _ in range(length):
                node = queue.popleft()
                sum1 += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            av = sum1 / length
            result.append(av)
        return result