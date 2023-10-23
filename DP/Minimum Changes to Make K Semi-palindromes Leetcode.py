class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        div = defaultdict(lambda: [1])
        n = len(s)
        for d in range(2, n):
             for v in range(d + d, n + 1, d):
                div[v].append(d)
        @cache
        def semi(string):
            n = len(string)
            if n == 1:
                return float('inf')
            min_change = float('inf')
            for d in div[n]:
                this = {}
                count = 0
                for j in range(len(string)):
                    if j%d not in this:
                        this[j%d] = []
                    this[j%d].append(string[j])
                for _ in this:
                    i = 0
                    j = len(this[_])-1
                    while i < j:
                        if this[_][i] != this[_][j]:
                            count += 1
                        i += 1
                        j -= 1
                min_change = min(min_change, count)
            return min_change
        @cache
        def recursion(i, k):
            if i == len(s) and k == 0:
                return 0
            if i == len(s):
                return float('inf')
            if k == 0:
                return semi(s[i:])
            ans = float('inf')
            n = len(s)
            for j in range(i, n-1):
                x = recursion(j+1, k-1) + semi(s[i:j+1])
                ans = min(ans, x)
            return ans
        return recursion(0, k-1)
