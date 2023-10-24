class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = [0 for i in range(n)]
        max_so_far = 0
        for i in range(n-1, -1, -1):
            maxi[i] = max_so_far
            max_so_far = max(max_so_far, nums[i])
        # print(maxi) 
        max_so_far = nums[0]
        ans = 0
        for j in range(1, n-1):
            ans = max((max_so_far - nums[j])*maxi[j] , ans)
            # print(ans, max_so_far)
            max_so_far = max(max_so_far, nums[j])
        return ans
