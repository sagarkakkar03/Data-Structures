class Solution:
	def findSubstring(self, A, B):
        word_len = len(B[0])
        if len(A) < len(B)*word_len:
            return []
        this = {}
        for i in B:
            if i not in this:
                this[i] = 0
            this[i] += 1
        i = 0
        j = len(B)*word_len
        ans = []
        while j <= len(A):
            that = {}
            flag = True
            for _ in range(i, len(B)*word_len+i, word_len):
                x = A[_:word_len+_]
                if x not in that:
                    that[x] = 0
                that[x] += 1
                if x not in this or that[x] > this[x]:
                    flag = False
                    break
            if flag:
                ans.append(i)                    
            i += 1
            j += 1
        return ans
