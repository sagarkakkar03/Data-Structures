from collections import Counter
class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        this = Counter(nums)
        def binSearch(ans):
            nonlocal this
            flag = True
            for i in this:
                if this[i]%ans != 0 and this[i]% ans != 1:
                    print(this[i], ans)
                    flag = False
                    break
            if flag == True:
                return True
            for i in this:
                if this[i]%ans != 0 and this[i]%ans != 1:
                    return False
            return True
        print(this)
        lo = 1
        hi = len(nums)
        value = -1
        while lo <= hi:
            mid = (lo+hi)//2
            print(mid)
            if binSearch(mid):
                value = mid 
                hi = mid-1
            else:
                lo = mid+1
        return value
