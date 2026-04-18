# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter=0
    def calculateheight(self,root):
        if not root:
            return 0
        leftheight=self.calculateheight(root.left)
        rightheight=self.calculateheight(root.right)

        self.diameter=max(self.diameter,leftheight+rightheight)

        return 1+max(leftheight, rightheight)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.calculateheight(root)
        return self.diameter
