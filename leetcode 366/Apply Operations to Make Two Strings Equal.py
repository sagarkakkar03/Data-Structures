class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diff = []
        for i, j in enumerate(s1):
            if j != s2[i]:
                diff.append(i)
        # print(diff)
        if len(diff)%2 == 1:
            return -1
        @cache
        def recursion(i, flip):
            if i == len(diff) and flip == None:
                return 0
            if i == len(diff):
                return float('inf')
            # print(i,flip)
            if flip != None:
                a = b = float('inf')
                if i + 1 < len(diff):
                    a = recursion(i+2, flip)+diff[i+1]-diff[i]
                b = recursion(i+1, None) + x
                return min(a, b)
            else:
                return min(recursion(i+2, flip) + diff[i+1] - diff[i], recursion(i+1, True))
        return recursion(0, None)
