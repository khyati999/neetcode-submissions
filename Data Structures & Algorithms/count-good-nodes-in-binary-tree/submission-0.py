# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, MaxVal):

            if not node:
                return 0
            
            ans=1 if node.val>=MaxVal else 0
            MaxVal=max(MaxVal, node.val)
            ans += dfs(node.left, MaxVal) 
            ans += dfs(node.right, MaxVal)
            return ans
        return dfs(root, root.val)
