import sys
sys.setrecursionlimit(10**6)
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	def t2Sum(self, A, B):
		this = set()
		ans = 0
		def tree(root):
			nonlocal this, B, ans
			if B - root.val in this: 
				ans = 1
			this.add(root.val)
			if root.left:
				tree(root.left)
			if root.right:
				tree(root.right)
		tree(A)
		return ans
