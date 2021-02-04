"""
Given the roots of two binary trees p and q, write a function to check if 
they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None:
            return False
        if q is None:
            return False
        if p.val != q.val:
            return False
        leftIsSame = self.isSameTree(p.left, q.left)
        rightIsSame = self.isSameTree(p.right, q.right)
        return leftIsSame and rightIsSame
