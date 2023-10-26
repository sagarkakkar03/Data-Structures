from heapq import *
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    next_greatest = [-1 for i in range(n)]
    prev_greatest = [-1 for i in range(n)]
    max_so_far = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > max_so_far:
            max_so_far = arr[i]
        else:
            next_greatest[i] = max_so_far
    max_so_far = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_so_far:
            max_so_far = arr[i]
        else:
            prev_greatest[i] = max_so_far
    ans = 0
    for i in range(n):
        if next_greatest[i] == -1 or prev_greatest[i] == -1:
            ans += arr[i]
        else:
            ans += min(next_greatest[i], prev_greatest[i])
    # print(ans)
    print(ans)
