class Node():
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEndOfWord = False
class trie():
    def __init__(self):
        self.root = Node()
    def add(self, word):
        root = self.root
        for i in word:
            if not root.children[ord(i) - 97]:
                root.children[ord(i)-97] = Node()
            root = root.children[ord(i)-97]
        root.isEndOfWord = True
    def check(self, word):
        root = self.root 
        for i in word:
            if not root.children[ord(i)-97]:
                return False
            root = root.children[ord(i)-97]
        return root.isEndOfWord
class Solution:
	def solve(self, A, B):
        word = ''
        T = trie()
        for i in A:
            if i == '_':
                T.add(word)
                word = ''
            else:
                word += i 
        T.add(word)
        this = {}
        for _, i in enumerate(B):
            score = 0
            word = ''
            for j in i:
                if j  == '_':
                    if T.check(word):
                        score += 1
                    word = ''
                else:
                    word += j
            if T.check(word) :
                score += 1
            if score not in this:
                this[score] = []
            this[score].append(_)
        res = sorted(this.keys(), reverse = True)
        ans = []
        for i in res:
            for j in this[i]:
                ans.append(j)
        return ans
