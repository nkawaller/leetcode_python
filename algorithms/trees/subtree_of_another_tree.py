"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:

   4 
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s. 
"""
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None:
            return True
        if s is None:
            return False
        if self.areIdentical(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def areIdentical(self, r1, r2):
        if r1 is None and r2 is None:
            return True
        if r1 is None or r2 is None:
            return False
        return (r1.val == r2.val and
                self.areIdentical(r1.left, r2.left) and
                self.areIdentical(r1.right, r2.right)
                )


"""
Alternate solution
"""


def is_subtree(big, small):
    flag = False
    queue = collections.deque()
    queue.append(big)
    while queue:
        node = queue.popleft()
        if node.val == small.val:
            flag = comp(node, small)
            break
        else:
            queue.append(node.left)
            queue.append(node.right)
    return flag


def comp(p, q):
    if p is None and q is None:
        return True
    if p is not None and q is not None:
        return p.val == q.val and comp(p.left, q.left) and comp(p.right, q.right)
    return False
