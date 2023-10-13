class Solution:
	# @param A : integer
	# @param B : list of list of integers
	# @return a list of list of integers
	def solve(self, B, A):
		n = len(A)
		m = len(A[0])
		matrix = [[[-1 for i in range(B+1)] for j in range(m)] for k in range(n)]
		for k in range(B+1):
			for i in range(n):
				for j in range(m):
					if k == 0:
						matrix[i][j][0] = A[i][j]
					else:
						a = b = c = d = 0
						if i-1 >= 0:
							a = matrix[i-1][j][k-1]
						if j-1 >= 0:
							b = matrix[i][j-1][k-1]
						if i + 1 < n:
							c = matrix[i+1][j][k-1]
						if j +1 < m:
							d=  matrix[i][j+1][k-1]
						matrix[i][j][k] = max(A[i][j], a, b, c, d)
		ans = []
		for i in range(n):
			row = []
			for j in range(m):
				row.append(matrix[i][j][B])
			ans.append(row)
		return ans
