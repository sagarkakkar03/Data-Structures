class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        n = len(A)
        total = sum(A)
        DP = [set() for i in range(n//2+1)]
        DP[0].add(0)
        for num in A:
            # print(num)
            for count in range(len(DP)-2, -1, -1):
                for a in DP[count]:
                    DP[count+1].add(a+num)
            # print(DP, count)
        for size in range(1, len(DP)):
            if (total*size)/n in DP[size]:
                return True 
        return False
