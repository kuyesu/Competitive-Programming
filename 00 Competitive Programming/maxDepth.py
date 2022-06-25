# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

class Solution:
  def maxDepth(self, roote) :
    if not root:
      return 0
    leftDepth = rightDepth = 0
    if root.left: leftDepth = self.maxDepth(root.left)
    if root.right: rightDepth = self.maxDepth(root.right)
    return max(leftDepth, rightDepth) + 1
      
a = [3,9,20,None,None,15,7]
s = Solution()

root = TreeNode(a)
s.maxDepth(root)