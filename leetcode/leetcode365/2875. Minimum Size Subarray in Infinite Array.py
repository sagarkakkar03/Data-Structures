class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        x = sum(nums) 
        sumNums = 0
        i = 0
        j = 0
        ans = float('inf')
        length = (target//x)*n
        sumNums = x*(length//n)
        while True:
            if sumNums == target:
                # print(i, j, length)
                ans = min(ans, length)
            if sumNums <= target:
                sumNums += nums[j%n]
                j += 1
                length += 1
            else:
                sumNums -= nums[i%n]
                i += 1
                length -= 1
                if i == len(nums):
                    return -1 if ans == float('inf') else ans
