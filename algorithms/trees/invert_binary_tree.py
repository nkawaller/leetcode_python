"""
Invert a binary tree.

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Time = O(n)
# Space = O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        else:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)

            root.left = right
            root.right = left
        return root