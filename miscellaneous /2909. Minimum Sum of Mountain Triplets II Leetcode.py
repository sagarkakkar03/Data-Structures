class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [-1 for _ in range(n)]
        post = [-1 for _ in range(n)]
        
        mini = float('inf')
        mini2= float('inf')
        ans = float('inf')
        for i in range(n):
            pre[i] = mini
            mini = min(nums[i], mini)
            post[n-i-1] = mini2 
            mini2 = min(nums[n-i-1], mini2)
        for j in range(1, n-1):
            if pre[j] < nums[j] > post[j]:
                ans = min(pre[j] + post[j] + nums[j], ans)
        return ans if ans != float('inf') else -1
