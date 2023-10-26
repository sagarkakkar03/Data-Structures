# from collections import Counter
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = [-1 for i in range(n)]
    arr2 = [i+1 for i in range(m)]
    for i in range(0, n, m):
        this = set(arr2)
        for j in range(i, min(i+m, n)):
            if arr[j] in this:
                ans[j] = arr[j]
                this.remove(arr[j])
        for j in range(i, min(i+m, n)):
            if ans[j] == -1: 
                ans[j] = this.pop()
    print(*ans)
