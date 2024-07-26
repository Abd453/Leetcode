"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        depth = 0
        if not root:
            return 0

        def dfs(node, curDepth):
            nonlocal depth
            if not node:
                return curDepth
            depth = max(depth, curDepth)
            for child in node.children:
                dfs(child, curDepth+1)
        
        dfs(root, 1)
        return depth