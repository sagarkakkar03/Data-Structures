import sys
sys.setrecursionlimit(10**6)
class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def isMatch(self, A, B):
        dp = [[-1 for i in range(len(B)+1)] for j in range(len(A)+1)]
        def match(i, j):
            nonlocal A, B, dp
            # print(i, j)
            if i == len(A) and j == len(B):
                return 1
            if i == len(A) or j == len(B):
                return 0
            if dp[i][j] != -1:
                return dp[i][j] 
            if j + 1 < len(B) and B[j+1] ==  '*':
                if A[i] == B[j] or B[j] == '.':
                    dp[i][j] = match(i+1, j) or match(i + 1, j + 2) or match(i, j+2)
                    return dp[i][j]
                else:
                    dp[i][j] = match(i, j+2)
                    return dp[i][j]
            elif A[i] == B[j] or B[j] == '.':
                dp[i][j] = match(i+1, j+1)
                return dp[i][j]
            else:
                return 0
        return match(0, 0)
