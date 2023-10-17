class Solution:  
	def avgset(self, A):
        n = len(A)
        total = sum(A)
		A.sort() 
        this = {}
        def possible(i, sumi, ele):
            nonlocal A
            nonlocal this
            if sumi < 0 or ele < 0:
                return False
            if sumi == 0 and ele == 0:
                return True
            if i >= len(A) or ele == 0:
                return False
            if (i, sumi, ele) in this:
                return this[(i, sumi, ele)]
            if sumi >= A[i]:
                this[(i, sumi, ele)] = possible(i+1, sumi - A[i], ele-1) or possible(i+1, sumi, ele)
                return possible(i+1, sumi - A[i], ele-1) or possible(i+1, sumi, ele)
            this[(i, sumi, ele)] = possible(i+1, sumi, ele)
            return possible(i+1, sumi, ele)
        I = None
        for size in range(1, len(A)//2+1):
            x = (total*size)/n
            if possible(0, x, size):
                I = size
                break
        if I == None:
            return []
        ans_dict = {}
        ans = []
        ans2 = []
        for i in range(len(A)):
            if possible(i, x-A[i], I-1):
                I -= 1
                ans.append(A[i])
                x -= A[i]
            else:
                ans2.append(A[i])
        return [ans, ans2]
