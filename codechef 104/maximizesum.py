def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = []
    for i, j in enumerate(arr):
        if i == 0:
            ans.append(j)
        else:
            factor = (m//j)*j
            while gcd(factor, arr[i-1]) != arr[i]:
                factor -= arr[i]
            ans.append(factor)
    print(*ans)
