from collections import deque
from heapq import *
class Solution: 
    def solve(self, A, B, C, D, E):
        adj = [[] for i in range(A+1)]
        for i in B:
            adj[i[0]].append((i[1], i[2]))
            adj[i[1]].append((i[0], i[2]))
        def dijkstra(origin, dis):
            # print(origin, 'origin')
            nonlocal adj
            queue =[]
            heapify(queue)
            heappush(queue, [0, origin])
            dis[origin] = 0
            while queue:
                _, node = heappop(queue)
                # print(node)
                for i in adj[node]:
                    # print(i)
                    # print(node, i[1], i[1])
                    if dis[node] + i[1] < dis[i[0]]:
                        dis[i[0]] = dis[node] + i[1]
                        heappush(queue, (dis[i[1]], i[0]))
        dis = [float('inf') for i in range(A+1)]
        dijkstra(C, dis)
        dis2 = [float('inf') for i in range(A+1)]
        dijkstra(D, dis2)
        # print(dis)
        # print(dis2)
        ans = dis[D]
        for i in E:
            ans = min(ans, dis[i[0]] + i[2] + dis2[i[1]], dis[i[1]] + i[2] + dis2[i[0]])
        return ans if ans != float('inf') else -1
