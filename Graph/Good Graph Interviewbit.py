from collections import Counter
class Solution:
    def solve(self, A):
        n = len(A)
        rank = [0 for i in range(n)]
        group = n
        def parent(index):
            while par[index] != index:
                index = par[index]
            return index
        def union(u, v):
            nonlocal group
            u = parent(u)
            v = parent(v)
            if u != v:
                if rank[u] > rank[v]:
                    par[v] = u 
                elif rank[v] >  rank[u]:
                    par[u] = v
                else:
                    par[u] = v
                    rank[v] += 1
                group -= 1
        par = [i for i in range(n)]
        for i in range(1, n):
            union(i, A[i]-1)
        return group - 1
