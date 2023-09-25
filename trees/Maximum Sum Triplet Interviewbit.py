class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.h = 1

class Tree:
    def __init__(self):
        self.ans = -1
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        root.h = 1 + max(self.get_height(root.left), self.get_height(root.right))
        b = self.balance(root)
        # print(b)
        if b < -1:
            temp = root
            root = root.right
            temp.right = root.left
            root.left = temp
        if b > 1:
            temp = root
            root = root.left
            temp.left = root.right
            root.right = temp
        if root.left:
            root.left.h = 1 + max(self.get_height(root.left.left), self.get_height(root.left.right))
        if root.right:
            root.right.h = 1 + max(self.get_height(root.right.left), self.get_height(root.right.right))
        return root

    def get_height(self, node):
        if node is None:
            return 0
        return node.h

    def balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def visualize(self, root, level=0, prefix="Root: "):
        if root is not None:
            print("Level", level, prefix, root.data)
            if root.left is not None or root.right is not None:
                self.visualize(root.left, level + 1, "L-- ")
                self.visualize(root.right, level + 1, "R-- ")
    def search(self, root, data):
        if root == None:
            return -1
        if self.ans < root.data < data:
            self.ans = root.data
        if root.data >= data:
            if root.left != None:
                return self.search(root.left, data)
            return -1
        else:
            if root.right!= None:
                return self.search(root.right, data)
            return root.data
    def preorder(self, root):
        if root is None:
            return
        self.preorder(root.left)
        self.preorder(root.right)

class Solution:
    def solve(self, A):
        t = Tree()
        root = None
        maxi = A[-1]
        ans = 0
        greater = [-1 for i in range(len(A))]
        for i in range(len(A)-1, -1, -1):
            if A[i] != max(maxi, A[i]):
                greater[i] = max(A[i], maxi)
            maxi = max(A[i], maxi)
        for i in range(len(A)):
            root = t.insert(root, A[i])
            t.search(root, A[i])
            if t.ans != -1 and greater[i] != -1:
                ans = max(ans, A[i] + t.ans + greater[i])
            t.ans = -1
        return ans
