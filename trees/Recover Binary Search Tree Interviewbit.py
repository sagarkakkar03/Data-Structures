import sys
sys.setrecursionlimit(10**6)
class Solution:
	def recoverTree(self, A):
        stack = []
        def push_left(root):
            nonlocal stack
            while root:
                stack.append(root)
                root = root.left
        def find_next():
            nonlocal stack
            node = stack.pop()
            if node.right:
                push_left(node.right)
            return node
        stack2 = []
        first_element = None
        second_element = None
        push_left(A)
        while stack:
            x = find_next()
            if first_element != None:
                if x.val < first_element.val:
                    if second_element == None:
                        second_element = x
                    else:
                        arr = [x, second_element]
                        arr.sort(key= lambda x:x.val)
                        second_element = arr[0]
            if stack2 == []:
                stack2.append(x)
            else:
                if stack2[-1].val > x.val:
                    if first_element == None:
                        first_element = stack2[-1]
                        second_element = x
                while stack2 and stack2[-1].val < x.val:
                    stack2.pop()
                stack2.append(x)
        return [second_element.val, first_element.val]
