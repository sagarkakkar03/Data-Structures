class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for a in  range(1, n+1):
            t = 0
            i = 1
            while i*i*a <= n:
                t += nums[i*i*a-1]
                i += 1
            ans = max(ans, t)
        return ans
