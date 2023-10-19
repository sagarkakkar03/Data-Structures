class Solution:
    def solve(self, A, B, C):
        n = len(A)
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]
        for i in range(n):
            if i != 0:
                prefix[i] += prefix[i-1] 
            if A[i] != B[i]:
                prefix[i] += 1
        for i in range(n-1, -1, -1):
            if i != n-1:
                suffix[i] += suffix[i+1] 
            if A[i] != B[i]:
                suffix[i] += 1
        ans = suffix[0]
        dp = [[-1 for i in range(n+1)] for j in range(n+1)]
        def rev(i, j):
            if j < i:
                return 0
            nonlocal A, B, dp
            if dp[i][j] != -1:
                return dp[i][j]
            if i == j:
                return int(A[i] != B[j])
            dp[i][j] = rev(i+1, j-1) + int(A[j] != B[i]) + int(A[i] != B[j])
            return dp[i][j]
        for i in range(n):
            for j in range(i+1, n):
                a = b = 0
                if i - 1 >= 0:
                    a = prefix[i-1]
                if j + 1 < n:
                    b = suffix[j+1]
                x = rev(i, j) + C
                ans = min(ans, a + x + b)
        return ans
