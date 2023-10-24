class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        arr = [-1 for i in range(n)]
        vis = [0 for i in range(n)]
        stack = []
        
        def dfs(i):
            vis[i] = 1
            if vis[edges[i]] == 0:
                dfs(edges[i])
            stack.append(i)
        
        for i in range(n):
            if vis[i] == 0:
                dfs(i)
        vis = [0 for i in range(n)]
        edges2 = [[] for i in range(n)]
        for i, j in enumerate(edges):
            edges2[j].append(i)
        def dfs2(i, stack2):
            stack2.append(i)
            vis[i] = 1
            for _ in edges2[i]:
                if vis[_] == 0:
                    dfs2(_, stack2)
        while stack:
            stack2 = []
            x = stack.pop()
            if vis[x] == 0: 
                print(x)
                dfs2(x, stack2)
            for i in stack2:
                arr[i] = len(stack2)
        # print(arr)
        def dfs3(i):
            if arr[i] != 1:
                return arr[i]
            return 1 + dfs3(edges[i])
        for i in range(n):
            arr[i] = dfs3(i)
        return arr
