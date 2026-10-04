# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def ValidCheck(node, left, right):
            if not node:
                return True
            if not(left<node.val<right):
                return False
            return ValidCheck(node.left, left, node.val) and ValidCheck(node.right, node.val, right)
        return ValidCheck(root, float("-inf"), float("inf"))
        