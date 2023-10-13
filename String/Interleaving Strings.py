class Solution:
	def isInterleave(self, A, B, C):
		if len(A) + len(B) != len(C):
			return 0
		matrix = [[[-1 for i in range(len(C)+1)] for j in range(len(B)+1)] for k in range(len(A)+1)]
		def mixing(i, j, k):
			nonlocal A, B, C, matrix
			if k == len(C):
				return 1
			if matrix[i][j][k] != -1:
				return matrix[i][j][k]
			a = 0
			if i < len(A) and A[i] == C[k]:
				matrix[i][j][k] = mixing(i+1, j, k+1)
				a = matrix[i][j][k] 
			b = 0
			if j < len(B) and B[j] == C[k]:
				matrix[i][j][k] = mixing(i, j+1, k+1)
				b = matrix[i][j][k] 
			return a or b
		return mixing(0,0,0)
