from math import *
from collections import deque
class Solution:
	def order(self, A, B):
        z = [x for x in zip(A, B)]
        z.sort()
        tree = [1 for i in range(len(A))]
        ans = [-1 for i in range(len(A))]
        tree = deque(tree)
        i = 0
        while True:
            if i >= len(tree) and log(i, 2) == int(log(i, 2)):
                break
            if i >= len(tree):
                tree.append(1)
            i += 1
        length = len(tree)-1
        i = len(tree)-2
        while i >= 0:
            tree.appendleft(tree[i]+tree[i+1])
            i -= 1
        def find(node, left, right, val):
            tree[node] -= 1
            if left == right:
                return left
            mid = (left + right)//2
            if tree[2*node+1] >= val:
                return find(2*node+1, left, mid, val)
            else:
                return find(2*node+2, mid+1, right, val- tree[2*node+1])
        low = 0
        high = len(A)
        height = []
        for i in z:
            pos = i[1]
            val = i[0]
            x = find(0, 0, len(tree)//2, i[1]+1)
            ans[x] = val
        return ans
