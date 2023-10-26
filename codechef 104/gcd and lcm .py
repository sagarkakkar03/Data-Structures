def gcd(a,b):
    if (b == 0):
         return a
    return gcd(b, a%b)
for _ in range(int(input())):
    x, y,k = map(int, input().split())
    i = 0
    while i < k and x != y:
        if x >y:
            y, x = x, y
        y = gcd(x, y)
        i += 1
    print(x+y)
