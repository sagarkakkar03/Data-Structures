class Solution:
	def solve(self, A):
		for row in range(1, len(A)):
			for col in range(len(A[0])):
				if A[row][col] != 0:
					A[row][col] += A[row-1][col]
		ans = 0
		for i in A:
			for i, j in enumerate(sorted(i, reverse = True)):
				ans = max(j*(i+1), ans)
		return ans
