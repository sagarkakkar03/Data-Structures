#author: Sushmanth

from sys import stdin
input = stdin.readline

inp = lambda : list(map(int,input().split()))

import heapq

def answer():


    ans = 0
    for i in range(n):
        q = []
        dist = [float('inf') for i in range(n)]
        dist[i] = 0
        heapq.heappush(q , [dist[i] , i])

        while(len(q)):
            d , u = heapq.heappop(q)
            if(d != dist[u]):continue

            for [v , w] in adj[u]:
                if(dist[v] > dist[u] + w):
                    dist[v] = dist[u] + w
                    heapq.heappush(q , [dist[v] , v])


        ans = max(ans , max(dist))


    return ans
  
    
for T in range(int(input())):

    n = int(input())
    a = inp()

    adj = [[] for i in range(n + 1)]
    for i in range(1 , n):
        adj[i].append([i - 1 , 1])
        adj[i - 1].append([i , 1])


    take = [[a[i] , i] for i in range(n)]
    take.sort()

    for i in range(1 , n):
        w = abs(take[i][0] - take[i - 1][0])
        adj[take[i][1]].append([take[i - 1][1] , w])
        adj[take[i - 1][1]].append([take[i][1] , w])
    
    print(answer())

