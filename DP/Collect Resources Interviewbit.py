
class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        mod = 10**9+7
        res = 0
        n = len(A)
        m = len(A[0])
        dp = [0 for i in range(m)]
        ans = 0
        for i in range(n):
            # traverse all rows 
            res = 0
            for j in range(m):
                # we calculate till which column we have can move toward left
                ans += A[i][j]
                res += B[i][j] - A[i][j]
                dp[j] = max(0  if j == 0 else dp[j-1], res + dp[j])
            print(dp)
        #dp[m-1] represents till last column and row how much should go left
        return (ans + dp[m-1])%mod
