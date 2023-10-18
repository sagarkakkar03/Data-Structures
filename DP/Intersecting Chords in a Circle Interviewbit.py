class Solution:
	# @param A : integer
	# @return an integer
	def chordCnt(self, A):
		mod = 10**9+7
		catalan = [1, 1]
		for i in range(2, A+1):
			a = 0
			for j in range(i):
				a += (catalan[j]*catalan[i-j-1])%mod
			catalan.append(a%mod)
		return catalan[-1]
